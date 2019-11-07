from django import forms
from .models import Draft, Feedback


class WriteBox(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        model = Draft
        fields = ['text', ]


class FeedbackBox(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "mceNoEditor"}), label='')

    class Meta:
        model = Feedback
        fields = ['summary', 'progression', 'aural_quality', 'pov_clear', 'style_distinct', 'metaphors', 'setting_specfic', 'noun_specific', 'verb_specific', 'adjective_specific', 'worldview', 'emi', 'favorite_lines', 'comments']
