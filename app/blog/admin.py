from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ["title", "image", "published", "snippet", "date"]

admin.site.register(Post, PostAdmin)
