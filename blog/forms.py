from django import forms
from .models import Blog,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=["title","tag_word","intro","body"]

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["name","body"]