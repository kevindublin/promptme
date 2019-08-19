from django.db import models
from tinymce.widgets import TinyMCE
from django import forms


class Form(forms.ModelForm):
    ...
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    ...
