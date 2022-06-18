from django.urls import path
from . import views
# Create a URl for each page and views function
urlpatterns = [
    path('userregister', views.userregister, name='userregister')
]