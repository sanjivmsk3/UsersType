from django.contrib.auth.forms import UserCreationForm
from app.models import User


class AllSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','profile_picture','email','password1','password2','place','city','state','pincode']