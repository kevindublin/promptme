from django.db import models
from django.conf import settings
from tinymce.widgets import TinyMCE
from django import forms


class PostForm(forms.ModelForm):
    ...
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    ...


class Draft(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.TextField(max_length=1100)

    created = models.DateTimeField(auto_now_add=True)
    revised = models.DateTimeField(auto_now=True)

    prompt = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="prompt_title",
    )
