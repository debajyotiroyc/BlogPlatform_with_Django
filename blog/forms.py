from .models import Blog,Comment
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=["title","slug","tag_word","intro","body"]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["name","body"]

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': '*Your first name..'}))
    last_name = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': '*Your last name..'}))

    username = forms.EmailField(max_length=254, required=True,
                                widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password..', 'class': 'password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..', 'class': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)

