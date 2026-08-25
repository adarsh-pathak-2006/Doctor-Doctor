from django.urls import path
from .views import RegisterView, LoginView, LogoutView, HomeView, IndividualPrescriptionView, PrescriptionView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', LoginView.as_view(), name='login'),
    path('opd/', HomeView.as_view(), name='home'),
    path('opd/<int:id>/', IndividualPrescriptionView.as_view(), name='prescription'),
    path('prescribe/', PrescriptionView.as_view(), name='create_prescription'),
    path('logout/', LogoutView, name='logout'),
]
