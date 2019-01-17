from django.contrib import admin

# Register your models here (classes)
from .models import Post

admin.site.register(Post)