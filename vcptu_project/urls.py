
from django.urls import path

from . import views

app_name = 'vcptu_project'

urlpatterns = [
    path('', views.projectPage, name="projectPage")
]
