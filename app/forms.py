from django.contrib.auth.forms import UserCreationForm
from app.models import User, Post, Categories, BookAppointment
from django import forms
from django.contrib.admin.widgets import AdminDateWidget


class AllSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','profile_picture','email','password1','password2','place','city','state','pincode']


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'



class BookAppointmentForm(forms.ModelForm):
    class Meta:
        model = BookAppointment
        fields = ('speciality','time',)

