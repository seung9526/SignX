from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout as django_logout
from django.conf import settings



def index(request):
		return render(request, 'pkiproject/index.html')

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			new_user = authenticate(username=form.cleaned_data['username'],
									password=form.cleaned_data['password1'],
									)
			login(request, new_user)
			return redirect(settings.LOGIN_REDIRECT_URL)
	else:
		form = SignupForm()
	return render(request, 'account/signup.html', {
		'form': form,
	})


def signin(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('pkiproject:index')
		else:
			return HttpResponse('로그인 실패. 다시 시도 해보세요.')
	else:
		form = LoginForm()
		return render(request, 'account/signin.html', {'form': form})


def logout(request):
	django_logout(request)
	return render(request, 'pkiproject/index.html')

def car_form(request):
   return render(request, 'pkiproject/car_form.html')