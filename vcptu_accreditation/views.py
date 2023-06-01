from django.shortcuts import render

# Create your views here.
def accreditationPage(request):
    template_name = 'accreditationPage/accreditationPage.html'
    context = {

    }

    return render(request, template_name, context)