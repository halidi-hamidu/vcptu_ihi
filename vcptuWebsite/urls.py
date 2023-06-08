"""
URL configuration for vcptuWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vcptu_home.urls', namespace='vcptu_home')),
    path('about-us', include('vcptu_about.urls', namespace='vcptu_about')),
    path('facility', include('vcptu_facility.urls', namespace='vcptu_facility')),
    path('team', include('vcptu_team.urls', namespace='vcptu_team')),
    path('publications', include('vcptu_publication.urls', namespace='vcptu_publication')),
    path('projects', include('vcptu_project.urls', namespace='vcptu_project')),
    path('acreditation', include('vcptu_accreditation.urls', namespace='vcptu_accreditation')),
    path('our-contacts', include('vcptu_contact.urls', namespace='vcptu_contact')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)