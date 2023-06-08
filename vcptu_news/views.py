from django.shortcuts import render

# Create your views here.
def newsPage(request):
    template_name = 'newsPage/newsPage.html'
    context = {

    }
    return render(request, template_name, context)