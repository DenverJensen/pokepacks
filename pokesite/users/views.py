import re
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Welcome '+username+'! please login')
        return redirect('/login')


    form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})

def profile (request):
    return render(request, 'users/profile.html')