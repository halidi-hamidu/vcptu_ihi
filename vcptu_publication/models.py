from django.db import models

import uuid
# Create your models here.
class PublicationModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    publication_title = models.CharField(max_length=5000, null=True, blank=True)
    publication_contributors = models.CharField(max_length=5000, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'List of Publications'

    def __str__(self):
        return str(self.publication_title)