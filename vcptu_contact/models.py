from django.db import models
import uuid 
# Create your models here.
class ContactModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
   
    full_name = models.CharField(max_length=100, null=True, blank=True)
    email_address = models.CharField(max_length=300, null=True, blank=True)
    message_body = models.CharField(max_length=300, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Visitors Response'

    def __str__(self):
        return str(self.full_name)