from django.db import models
from django.contrib.auth.models import User
from cms.models.fields import PlaceholderField
from filer.fields.image import FilerImageField
from blog.slug import unique_slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    text = PlaceholderField("blog_text")
    image = FilerImageField(blank=True, null=True)
    slug = models.SlugField(unique=False, default = "sluggymcslugface")
    published = models.BooleanField(default = False)
    snippet = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug = self.title
        unique_slugify(self, slug)
        super(Post, self).save(*args, **kwargs)
