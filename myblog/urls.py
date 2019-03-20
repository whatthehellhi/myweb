from . import views
from django.urls import path,re_path

urlpatterns = [
    path('',views.blog_list,name ='blog_list'),
    path('<int:blog_pk>', views.blog_details, name='blog_details'),
    path('type/<int:blog_type_pk>', views.blog_Type, name='blog_Type'),
]
