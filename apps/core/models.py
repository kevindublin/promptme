from django.db import models
from tinymce.widgets import TinyMCE
from django import forms
from tinymce.models import HTMLField


class PostForm(forms.ModelForm):
    ...
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    ...


class WriteBox(models.Model):
    ...
    content = HTMLField()
    ...
