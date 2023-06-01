from django.shortcuts import render

# Create your views here.
def projectPage(request):
    template_name = 'projectPage/projectPage.html'
    context = {

    }
    return render (request, template_name, context)