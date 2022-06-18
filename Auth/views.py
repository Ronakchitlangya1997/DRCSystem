from django.shortcuts import render, redirect
from Auth.forms import createUserForm
from Auth.models import DRCUser
import random
from django.contrib.auth import authenticate, login as UserLogin, logout as UserLogout
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


def loginWithPhoneNumberOTP(request):
    userphonenumbermessage = False
    if request.method == 'POST':
        PhoneNumber = request.POST['Phonenumber']  
        if DRCUser.objects.filter(Phone_number=PhoneNumber).exists():
            drcUserData = DRCUser.objects.get(Phone_number=PhoneNumber)
            drcUserData.OTP_code = random.randrange(100000,999999)
            drcUserData.save()
            request.session['PhoneNumber'] = PhoneNumber
            return redirect('VerifyOTP')
        else:
            userphonenumbermessage = True
    
    context = {'userphonenumbermessage': userphonenumbermessage}

    return render(request, 'verifiedphonenumber.html', context)

def VerifyOTP(request):
    OTPVerificationmessage = False
    Phonenumber = request.session['PhoneNumber']
    if request.method == "POST":
        userOTPCode = request.POST['OTPCode']
        drcUserData = DRCUser.objects.get(Phone_number=Phonenumber)
        print(drcUserData.OTP_code)
        if (drcUserData.OTP_code == int(userOTPCode)):
            request.session['PhoneNumber'] = Phonenumber
            return redirect('login')
        else:
            OTPVerificationmessage = True
    context = {'OTPVerificationmessage': OTPVerificationmessage}
    return render(request, 'GetOTPlogin.html', context)

def login(request):
    loginErrorMessage = False
    Phonenumber = request.session['PhoneNumber']
    if request.method == 'POST':
        Username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, Phone_number=Phonenumber, username=Username, password=password)
        if user is not None:   
            UserLogin(request, user)
            return redirect('Home') 
        else:    
            loginErrorMessage = True
    context={'loginErrorMessage': loginErrorMessage}
    return render(request, 'login.html', context)

def logout(request):
    UserLogout(request)
    return redirect('loginWithPhoneNumberOTP')

