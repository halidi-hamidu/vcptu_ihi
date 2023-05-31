from django.db import models
import uuid
from ckeditor.fields import RichTextField
# Create your models here.
class NewsModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    upload_image = models.ImageField(upload_to='media')
    news_main_title = models.CharField(max_length=1000, null=True, blank=True)
    descriptions = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Latest news'

    def __str__(self):
        return str(self.news_main_title)