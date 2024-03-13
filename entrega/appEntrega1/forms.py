from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=300)
    subtitle = forms.CharField(max_length=900)
    content = forms.CharField(max_length=10000)
    category = forms.CharField(max_length=45)

class ContactMessageForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    message = forms.CharField(max_length=700)

class TeamMemberForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.EmailField()
    githubaccount = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    first_name= forms.CharField(label='Nombre',required=False)
    last_name= forms.CharField(label='Apellido',required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class UserUpdateForm(UserCreationForm):
    email=forms.EmailField()
    first_name= forms.CharField(label='Nombre',required=False)
    last_name= forms.CharField(label='Apellido',required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}
