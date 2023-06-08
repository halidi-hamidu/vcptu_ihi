from django.shortcuts import render
from .models import NewsModel
# Create your views here.
def newsPage(request):

    get_all_news = NewsModel.objects.all().order_by('-created_at')
    template_name = 'newsPage/newsPage.html'
    context = {
        'get_all_news':get_all_news
    }
    return render(request, template_name, context)