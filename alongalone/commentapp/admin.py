from django.contrib import admin
from .models import Comment
# Register your models here
#/admin사이트에서 Comment를 관리할수 있도록 만듬
admin.site.register(Comment)