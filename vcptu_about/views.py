from django.shortcuts import render

# Create your views here.




def aboutPage(request):
    
    template_name = 'aboutPage/aboutPage.html'
    context ={
        

    }
    return render(request, template_name, context)