from django.db import models
from django.contrib.auth.models import User

def post_upload_handler(instance, filename):
    return '{author}/posts/{slug}/images/{filename}'.format(author=instance.author.username,
                                                            slug=instance.slug,
                                                            filename=filename)

class Post(models.Model):
    title = models.CharField(max_length=255,)
    author = models.ForeignKey(User, related_name='posts')
    date_created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to=post_upload_handler, blank=True, null=True)

    def __str__(self):
        return self.title

