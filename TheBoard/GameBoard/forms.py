from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(min_length=50)

    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'type', 'upload']

