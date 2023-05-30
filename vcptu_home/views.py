from django.shortcuts import render
from vcptu_publication.models import *
# Create your views here.

def homePage(request):
    get_latest_publication = PublicationModel.objects.all().order_by('-created_at')[0:2]
    template_name = 'homePage/homePage.html'
    context ={
        'get_latest_publication':get_latest_publication
    }
    return render(request, template_name, context)