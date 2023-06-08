

from .models import *
from django.forms import ModelForm

class ContactModelForm(ModelForm):
  class Meta:
    model =ContactModel
    fields = '__all__'
    exclude =[
      'created_at',
      'updated_at'
    ]