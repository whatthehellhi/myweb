from django.db import models
from django.contrib.auth.models import User

class blogtype(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    type_blog = models.ForeignKey(blogtype,on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<blog:%s>'%self.title
