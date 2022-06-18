from django.shortcuts import render, redirect
from Auth.forms import createUserForm
from Auth.models import DRCUser
# Create your views here.

# Registration page function
def userregister(request):
    welcomeMessage = False
    userform = createUserForm()
    if request.method == "POST":
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            welcomeMessage = True

    context={'form':userform, 'welcomeMessage': welcomeMessage}

    return render(request, 'userregister.html', context)
