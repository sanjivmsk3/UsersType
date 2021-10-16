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
    path('patient-dashboard',Patient_Dashboard.as_view(),name='patientDashboard'),

    path('all-blog-post', AllPost.as_view(), name='allblog'),
    path('add-blog-post', AddPost.as_view(), name='addpost'),
    path('all-blog-category', AllCategory.as_view(), name='allcategory'),
    path('add-blog-category', AddCategory.as_view(), name='addcategory'),
    path('all-blog-draft-post', AllDraftPost.as_view(), name='draftpost'),
    path('all-blog-posts/<int:id>/', CategoryPostFilter.as_view(), name='catfilter'),
    path('patient-lists', Patient_lists.as_view(), name='patientlist'),
    path('allow-patient/<int:id>', Allow_Post.as_view(), name='allowpatient'),
    path('patient-dash', PatientDash.as_view(), name='patientDsh'),
    path('patient-add-post', PatientAddPost.as_view(), name='patientaddpost'),
    path('patient-all-post', PatientAllPost.as_view(), name='patientallpost'),
    path('patient-all-draft-post', PatientAllDraftPost.as_view(), name='patientalldraftpost'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)