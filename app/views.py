from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from app.forms import AllSignupForm

# Create your views here.
class Home(View):
    def get(self, request):
        if request.user.is_staff:
            return redirect('doctorDashboard')
        elif request.user.is_active:
            return redirect('patientDashboard')
        else:
            form = AllSignupForm
            return render(request, 'patient_signup.html',{'forms':form, "title":"Create Patient Account"})

    def post(self, request):
        form = AllSignupForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            #msg
            return redirect('home')

class All_Logins(View):
    def get(self, request):
        if request.user.is_staff:
            return redirect('doctorDashboard')
        elif request.user.is_active:
            return redirect('patientDashboard')
        else:
            return render(request, 'login.html',{"title":"Patient/Doctor Login"})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)
        except:
            #msg username or password not exists
            return redirect('login')

        if user is not None:
            login(request, user)
            if request.user.is_staff is True:
                #msg logged in Doctor
                return redirect('doctorDashboard')
            elif request.user.is_active is True:
                # msg logged in patient
                return redirect('patientDashboard')
            else:
                logout(request)
                # msg logout
                return redirect('login')
        else:
            # msg username or password not exists
            return redirect('login')


class LogOut(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        #msg
        return redirect('login')


class Doctor_Signup(View):
    def get(self, request):
        if request.user.is_staff:
            return redirect('doctorDashboard')
        elif request.user.is_active:
            return redirect('patientDashboard')
        else:
            form = AllSignupForm
            return render(request, 'doctor_signup.html',{'forms':form,"title":"Create Doctor Account"})

    def post(self, request):
        form = AllSignupForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.is_staff = True
            f.save()
            return redirect('login')
        else:
            # msg
            return redirect('home')

class Doctor_Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            return render(request, 'doctor_dashboard.html',{"title":"Doctor Dashboard"})
        else:
            logout(request)
            return redirect('login')

class Patient_Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_active:
            return render(request, 'patient_dashboard.html',{"title":"Patient Dashboard"})
        else:
            logout(request)
            return redirect('login')

