from django.db import models
from imagekit.models import ProcessedImageField

# Create your models here.
class Post(models.Model):
    titel = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True,
        )