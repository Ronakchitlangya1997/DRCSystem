from django.urls import path
from . import views
# Create a URl for each page and views function
urlpatterns = [
    path('userregister', views.userregister, name='userregister'),
    path('', views.loginWithPhoneNumberOTP, name='loginWithPhoneNumberOTP'),
    path('VerifyOTP', views.VerifyOTP, name='VerifyOTP'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]