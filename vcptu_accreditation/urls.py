
from django.urls import path

from . import views

app_name = 'vcptu_accreditation'

urlpatterns = [
    path('', views.accreditationPage, name="accreditationPage")
]
