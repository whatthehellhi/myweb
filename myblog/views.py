from django.shortcuts import render_to_response,get_object_or_404
from .models import blog,blogtype

def blog_list (request):
    context = {}
    context['blogs'] = blog.objects.all()
    context['types'] = blogtype.objects.all()
    return  render_to_response('blog_list.html',context)

def blog_details (request,blog_pk):
    context = {}
    context['blogdetails'] = get_object_or_404(blog,pk=blog_pk)
    return render_to_response('blog_details.html',context)

def blog_Type (request,blog_type_pk):
    context = {}
    blog_type = get_object_or_404(blogtype,pk=blog_type_pk)
    context['blogtypes'] = blog.objects.filter(type_blog=blog_type)
    context['blog_types'] = blog_type
    return render_to_response('blog_type.html',context)