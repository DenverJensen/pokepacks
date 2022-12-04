from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='index'),
    path('home/', views.home, name='home'),
   

]