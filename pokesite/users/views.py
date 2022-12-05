import re
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def register(request):
		form = UserCreationForm()
				
		if request.method == "POST":

				form = UserCreationForm(request.POST)

				if form.is_valid():
						user = form.save(commit=False)

						user.is_valid = False
						user.save()
						username = form.cleaned_data.get('username')
						messages.success(request, 'Welcome '+username+'! please login')
						return redirect('/login')
				else:
						messages.warning(request, 'Invalid registration details')
						
		return render(
				request, "users/register.html",
				{"form": form}
		)

def profile (request):
    return render(request, 'users/profile.html')