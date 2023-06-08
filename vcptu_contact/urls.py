
from django.urls import path

from . import views

app_name = 'vcptu_contact'

urlpatterns = [
    path('', views.contactPage, name="contactPage")
]
