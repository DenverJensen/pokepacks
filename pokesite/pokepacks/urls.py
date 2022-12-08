from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='index'),
    path('home/', views.home, name='home'),
    path('open/', views.openPacks, name='open'),
    path('load/', views.loadPacks, name='loadPacks'),

]