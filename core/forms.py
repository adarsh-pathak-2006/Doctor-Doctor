from django import forms
from .models import Prescription

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model=Prescription
        fields=['age', 'condition', 'prior_medical_history']