from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],password=cd['password'])
			if user is not None:
				login(request, user)
				return HttpResponse('Authenticated successfully')
			else:
				return HttpResponse('Disabled account')
		else:
			return HttpResponse('Invalid Login')
	else:
		form = LoginForm()
	return render(request, 'login/index.html', {'form': form})

@login_required
def dashboard(request):
	return render(request, 'login/dashboard.html', {'section': 'dashboard'})

# Create your views here.
def index(request):
	print('home'*50)