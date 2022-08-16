from django.contrib import admin
<<<<<<< HEAD
from .models import Blog

admin.site.register(Blog)
=======
from .models import Blog, Comment

admin.site.register(Blog)
admin.site.register(Comment)
>>>>>>> main-1
