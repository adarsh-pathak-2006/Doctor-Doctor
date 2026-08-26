from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm, PrescriptionForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Prescription
from services.response import final_response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit

@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
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

@method_decorator(ratelimit(key='ip', rate='10/m', block=True), name='dispatch')
@method_decorator(ratelimit(key='post:username', rate='5/m', block=True), name='post')
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
                return redirect('home')
            return render(request, 'login.html', { 'form':form_data, 'user_err':'user does not exist try registration first' })
        return render(request, 'login.html', { 'form':form_data, 'form_err':form_data.errors })

@login_required
@ratelimit(key='user', rate='10/m', block=True)
def LogoutView(request):
    logout(request)
    return redirect('login')

@method_decorator(ratelimit(key='user', rate='30/m', block=True), name='dispatch')
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        data=Prescription.objects.filter(user=request.user)
        form=PrescriptionForm()
        return render(request, 'home.html', {'data':data, 'form':form})

@method_decorator(ratelimit(key='user', rate='30/m', block=True), name='dispatch')
class IndividualPrescriptionView(LoginRequiredMixin, View):
    def get(self, request, id):
        data=get_object_or_404(Prescription, user=request.user, id=id)
        return render(request, 'individual.html', {'data':data})

@method_decorator(ratelimit(key='user', rate='5/m', block=True), name='dispatch')
@method_decorator(ratelimit(key='user', rate='20/d', block=True), name='dispatch')
class PrescriptionView(LoginRequiredMixin, View):
    def post(self, request):
        form_data=PrescriptionForm(request.POST)
        data=Prescription.objects.filter(user=request.user)
        if form_data.is_valid():
            age=form_data.cleaned_data['age']
            condition=form_data.cleaned_data['condition']
            prior=form_data.cleaned_data['prior_medical_history']
            data=form_data.save(commit=False)
            ai_response=final_response(age=age, condition=condition, prior_conditions=prior)
            data.drug_prescription=ai_response.get('prescription')
            data.analysis=ai_response.get('condition_analysis')
            data.user=request.user
            data.save()
            return render(request, 'individual.html', {'data':data})
        return render(request, 'home.html', {'data':data, 'form':form_data, 'form_err':form_data.errors})
        