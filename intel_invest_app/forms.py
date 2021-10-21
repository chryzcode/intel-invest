from django.forms import ModelForm
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length = 100)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('full_name', 'username', 'email','password1', 'password2')

    def __init__ (self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)