from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from app.forms import AllSignupForm, AddPostForm, AddCategoryForm, BookAppointmentForm
from app.models import Post, Categories, User, BookAppointment


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
            context = {
                "apo": BookAppointment.objects.filter(doctor=request.user),
                "title": "Doctor Dashboard"
            }
            return render(request, 'doctor_dashboard.html', context)
        else:
            logout(request)
            return redirect('login')

class Patient_Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_active:
            context = {
                "title": "Patient Dashboard",
                "allCategories": Categories.objects.all(),
                "allPosts": Post.objects.filter(draft="PUBLIC"),
                "allDoctors": User.objects.filter(is_staff=True),
                "apooint": BookAppointment.objects.filter(patient=request.user, status=True)
            }
            return render(request, 'patient_dashboard.html', context)
        else:
            logout(request)
            return redirect('login')


class AllPost(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            context = {
                'allPost': Post.objects.filter(draft="PUBLIC"),
                "title": "All Blog Post"
            }
            return render(request, 'all_post.html', context)
        else:
            logout(request)
            return redirect('login')


class AddPost(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            form = AddPostForm
            return render(request, 'add_post.html', {"forms":form})
        else:
            logout(request)
            return redirect('login')

    def post(self, request):
        if request.user.is_staff:
            form = AddPostForm(request.POST or None, request.FILES or None)

            if form.is_valid():
                f = form.save(commit=False)
                f.user = request.user
                f.save()
                return redirect('allblog')
            else:
                #msg
                return redirect('addpost')
        else:
            logout(request)
            return redirect('login')


class AllCategory(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            context = {
                'allCategory': Categories.objects.all(),
                "title": "All Blog Category"
            }
            return render(request, 'all_category.html', context)
        else:
            logout(request)
            return redirect('login')


class AddCategory(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            form = AddCategoryForm
            return render(request, 'add_category.html', {"forms":form})
        else:
            logout(request)
            return redirect('login')

    def post(self, request):
        if request.user.is_staff:
            form = AddCategoryForm(request.POST or None, request.FILES or None)

            if form.is_valid():
                f = form.save(commit=False)
                f.user = request.user
                f.save()
                return redirect('allcategory')
            else:
                #msg
                return redirect('addcategory')
        else:
            logout(request)
            return redirect('login')


class AllDraftPost(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            context = {
                'alldraftPost': Post.objects.filter(draft="DRAFT"),
                "title": "All Blog Draft Posts"
            }
            return render(request, 'draft.html', context)
        else:
            logout(request)
            return redirect('login')


class CategoryPostFilter(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_active:
            context = {
                "allCategories": Categories.objects.all(),
                'allPosts': Post.objects.filter(draft="PUBLIC", category_id=id),
            }
            return render(request, 'patient_dashboard.html', context)
        else:
            logout(request)
            return redirect('login')


class Patient_lists(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            context = {
                "title": "Patient Lists",
                "patientList": User.objects.filter(is_staff=False)
            }
            return render(request, 'all_patient_lists.html', context)
        else:
            logout(request)
            return redirect('login')


class Allow_Post(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            patient = User.objects.get(id=id)
            if patient.allow:
                patient.allow = False
                patient.save()
            else:
                patient.allow = True
                patient.save()
            return redirect('patientlist')
        else:
            logout(request)
            return redirect('login')


class PatientDash(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.allow:
            return render(request, 'patient_allow_dash.html', {"title":"Patient-Dashboard"})
        else:
            logout(request)
            return redirect('login')


class PatientAddPost(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.allow:
            form = AddPostForm
            return render(request, 'patient_add_post.html', {"forms":form})
        else:
            logout(request)
            return redirect('login')

    def post(self, request):
        if request.user.allow:
            form = AddPostForm(request.POST or None, request.FILES or None)

            if form.is_valid():
                f = form.save(commit=False)
                f.user = request.user
                f.save()
                return redirect('patientDashboard')
            else:
                #msg
                return redirect('patientaddpost')
        else:
            logout(request)
            return redirect('login')



class PatientAllPost(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.allow:
            context = {
                'patientAllPost': Post.objects.filter(draft="PUBLIC", user__allow=True, user=request.user),
                "title": "All Blog Post"
            }
            return render(request, 'patient_all_post.html', context)
        else:
            logout(request)
            return redirect('login')

class PatientAllDraftPost(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.allow:
            context = {
                'patientAllDraftPost': Post.objects.filter(draft="DRAFT", user__allow=True, user=request.user),
                "title": "All Blog Post"
            }
            return render(request, 'patient_draft_post.html', context)
        else:
            logout(request)
            return redirect('login')


class AppointmnetForm(View):
    def get(self, request, id):
        if request.user.is_active:
            form = BookAppointmentForm
            return render(request, 'appointement_form.html',{"forms":form, "id":id})
        else:
            logout(request)
            return redirect('login')
    def post(self, request, id):
        form = BookAppointmentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.doctor = User.objects.get(id=id)
            f.patient = request.user
            f.date = request.POST.get('date')
            f.save()
            print("save")
        else:
            print("not-save")
            return redirect('patientDashboard')
        return redirect('patientDashboard')


class AppointmentAprove(View):
    def get(self, request, id):
        apr = BookAppointment.objects.get(id=id)
        apr.status = True
        apr.save()
        return redirect('doctorDashboard')