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

def newsDetailPage(request, id):
    get_news_detail = NewsModel.objects.get(id = id )
    template_name = 'newsPage/newsDetailPage.html'
    context = {
        'get_news_detail':get_news_detail
    }
    return render(request, template_name, context)