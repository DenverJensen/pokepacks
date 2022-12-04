from django.shortcuts import render

from re import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.template import loader

# Create your views here.


def home(request):
    context = {
    }
    return render(request, 'pokepacks/home.html', context)