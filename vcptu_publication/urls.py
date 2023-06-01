
from django.urls import path

from . import views

app_name = 'vcptu_publication'

urlpatterns = [
    path('', views.publicationPage, name="publicationPage")
]
