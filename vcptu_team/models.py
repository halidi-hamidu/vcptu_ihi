from django.db import models
import uuid
from ckeditor.fields import RichTextField
# Create your models here.
class TeamModel(models.Model):
    STAFF_TITLE = (
        ('', 'Select Title'),
        ('Head of Unit', 'Head of Unit'),
        ('Test Facility Manager', 'Test Facility Manager'),
        ('Study Director', 'Study Director'),
        ('Project Manager', 'Project Manager'),
        ('Study Coordinator', 'Study Coordinator'),
        ('Technician', 'Technician'),
        ('Research Scientist', 'Research Scientist'),
        ('Data Manager', 'Data Manager'),
        ('Test Facility Coordinator', 'Test Facility Coordinator'),
        ('Administrative Officer', 'Administrative Officer'),

    )
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    image = models.ImageField(upload_to='media')
    staff_name = models.CharField(max_length=100, null=True, blank=True)
    staff_title = models.CharField(max_length=300, null=True, blank=True, choices=STAFF_TITLE)
    biography = RichTextField( default="No data")
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'VCPTU Team'

    def __str__(self):
        return str(self.staff_name)