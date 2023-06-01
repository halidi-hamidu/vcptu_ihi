from django.shortcuts import render

# Create your views here.
def publicationPage(request):
    template_name = 'publicationPage/publicationPage.html'
    context ={

    }

    return render (request, template_name, context)