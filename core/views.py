from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class RegisterView(View):
    def get(self, request):
        form=RegisterForm()
        return render(request, 'register.html', {'form':form})

    def post(self, request):
        form_data=RegisterForm(request.POST)
        if form_data.is_valid():
            username=form_data.cleaned_data['username']
            email=form_data.cleaned_data['email']
            password=form_data.cleaned_data['password']

            if User.objects.filter(Q(username=username) | Q(email=email)).exists():
                return render(request, 'register.html', {'form':form_data, 'user_err':'username or email already exists'})
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
        return render(request, 'register.html', { 'form':form_data, 'form_err':form_data.errors })

class LoginView(View):
    def get(self, request):
        form=LoginForm()
        return render(request, 'login.html', { 'form':form })

    def post(self, request):
        form_data=LoginForm(request.POST)
        if form_data.is_valid():
            username=form_data.cleaned_data['username']
            password=form_data.cleaned_data['password']
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shortner_home')
            return render(request, 'login.html', { 'form':form_data, 'user_err':'user does not exist try registration first' })
        return render(request, 'login.html', { 'form':form_data, 'form_err':form_data.errors })

@login_required
def LogoutView(request):
    logout(request)
    return redirect('login')
