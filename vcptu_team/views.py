from django.shortcuts import render
from .models import TeamModel
# Create your views here.
def teamPage(request):
    get_all_team = TeamModel.objects.all().order_by('created_at')
    template_name = 'teamPage/teamPage.html'
    context = {
        'get_all_team':get_all_team
    }

    return render(request, template_name, context)