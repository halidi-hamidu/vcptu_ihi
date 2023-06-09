from django.shortcuts import render
from vcptu_publication.models import *
from vcptu_team.models import *
from vcptu_news.models import NewsModel
# Create your views here.


def homePage(request):
    try:
        get_latest_news = NewsModel.objects.all().order_by('-created_at')[0:3]

        get_latest_publication = PublicationModel.objects.all().order_by('-created_at')[0:2]

        get_head_of_unit = TeamModel.objects.get(staff_title ='Head of Unit')
        get_test_facility_manager = TeamModel.objects.get(staff_title ='Test Facility Manager')
        get_study_director = TeamModel.objects.get(staff_title ='Study Director')
        get_project_manager = TeamModel.objects.get(staff_title ='Project Manager')
        get_all_team_leader = TeamModel.objects.all()
        template_name = 'homePage/homePage.html'
        context ={
            'get_latest_publication':get_latest_publication,
            'get_head_of_unit':get_head_of_unit,
            'get_test_facility_manager':get_test_facility_manager,
            'get_study_director':get_study_director,
            'get_project_manager':get_project_manager,
            'get_latest_news':get_latest_news,
            'get_all_team_leader':get_all_team_leader

        }
        return render(request, template_name, context)
    except:
        template_name = 'ErrorPage/page404.html'
        context = {

        }
        return render  (request, template_name, context)
    