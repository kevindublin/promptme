from django.db import models
from django.conf import settings
from tinymce.widgets import TinyMCE
from django import forms


class Draft(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.TextField(max_length=1400)

    created = models.DateTimeField(auto_now_add=True)
    revised = models.DateTimeField(auto_now=True)

    prompt = models.CharField(max_length=300)
    image = models.CharField(max_length=200)
    in_queue = models.BooleanField(default=False)
    received_feedback = models.BooleanField(default=False)
    feedback_amount = models.IntegerField(default=0)

    class Meta:
        ordering = ['revised']

    def __str__(self):
        return 'Draft {} by {}'.format(self.text, self.user)


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
        ('6', 'Surprised'),
        ('7', 'Moved')
    )
    draft = models.ForeignKey('Draft', on_delete=models.CASCADE, related_name='allfeedback')

    reader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    added = models.DateTimeField(auto_now=True)

    summary = models.TextField(max_length=500)
    progression = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    aural_quality = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    clear_pov = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    distinct_style = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    metaphors = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    specific_setting = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    specific_nouns = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    specific_verbs = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    specific_adjectives = models.CharField(max_length=1, choices=SURVEY_OPTIONS)
    clear_worldview = models.CharField(max_length=1, choices=SURVEY_OPTIONS)

    emi = models.CharField(max_length=1, choices=EMOTIONAL_IMPACT_INDEX)
    favorite_lines = models.TextField(max_length=500)
    comments = models.TextField(max_length=500)

    class Meta:
        ordering = ['-added']

    def __str__(self):
        return 'Feedback {} by {}'.format(self.comments, self.reader)
