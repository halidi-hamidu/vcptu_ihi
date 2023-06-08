from django.shortcuts import render, redirect
from .forms import ContactModelForm
from django.contrib import messages
# Create your views here.
def contactPage(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Message Sent Successful")
                return redirect('contactPage')
        except:
            messages.info(request, "Message Not Sent, please Try Again Later")
            return redirect('contactPage')
    template_name = 'contactPage/contactPage.html'
    context = {

    }
    return render(request, template_name, context)