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
    text = models.TextField(max_length=1400)

    created = models.DateTimeField(auto_now_add=True)
    revised = models.DateTimeField(auto_now=True)

    prompt = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    in_queue = models.BooleanField(default=False)


class Feedback(models.Model):
    SURVEY_OPTIONS = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('S', 'Somewhat')
    )
    EMOTIONAL_IMPACT_INDEX = (
        ('0', 'Indifferent'),
        ('1', 'Angry'),
        ('2', 'Disgusted'),
        ('3', 'Happy'),
        ('4', 'Sad'),
        ('5', 'Amused'),
        ('6', 'Surprised')
    )
    draft = models.ForeignKey('Draft', on_delete=models.CASCADE)

    reader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    added = models.DateTimeField(auto_now=True)

    summary = models.TextField(max_length=500)
    progression = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    aural_quality = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    pov_clear = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    style_distinct = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    metaphors = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    setting_specfic = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    noun_specific = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    verb_specific = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    adjective_specific = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    worldview = models.CharField(max_length=1, choices=SURVEY_OPTIONS)

    emi = models.CharField(max_length=1, choices=EMOTIONAL_IMPACT_INDEX)
    favorite_lines = models.TextField(max_length=500)
    comments = models.TextField(max_length=500)
