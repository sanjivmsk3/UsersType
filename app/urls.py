from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('doctor-signup',Doctor_Signup.as_view(),name='doctorSignup'),
    path('login',All_Logins.as_view(),name='login'),
    path('logout',LogOut.as_view(),name='logout'),
    path('doctor-dashboard',Doctor_Dashboard.as_view(),name='doctorDashboard'),
    path('patient-dashboard',Patient_Dashboard.as_view(),name='patientDashboard')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)