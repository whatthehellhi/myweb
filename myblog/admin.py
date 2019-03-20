from django.contrib import admin
from .models import blog,blogtype

@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ('title','content','author','type_blog','created_time','last_update_time')


@admin.register(blogtype)
class blogtypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')