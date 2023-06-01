from django.shortcuts import render
from vcptu_facility.models import *
# Create your views here.
def facilityPage(request):
    get_all_facility = FacilityModel.objects.all().order_by('-created_at')
    template_name = 'facilityPage/facilityPage.html'
    context = {
        'get_all_facility':get_all_facility
    }

    return render (request, template_name, context)