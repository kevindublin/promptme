from django import forms
from .models import Draft, Feedback


class WriteBox(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        model = Draft
        fields = ['text', ]


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput (attrs={'placeholder':'Name', 'class': 'form-control'}), label='')
    email = forms.EmailField(widget=forms.EmailInput (attrs={'placeholder':'you@example.com', 'class': 'form-control'}), label='')
    subject = forms.CharField(widget=forms.TextInput (attrs={'placeholder':'Subject', 'class': 'form-control'}), label='')
    message = forms.CharField(widget=forms.Textarea (attrs={'placeholder':'Your message...', 'class': 'form-control'}), label='')


class FeedbackBox(forms.ModelForm):
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

    summary = forms.CharField(widget=forms.Textarea(attrs={"class": "mceNoEditor"}), label='Write a brief summary of the draft:')
    progression = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label='Is there a throughline from beginning to end?')
    aural_quality = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label='When read aloud, is it rhythmic?')
    pov_clear = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label='Is the point of view/speaker clear?')
    style_distinct = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label='Is the writing style distinct?')
    metaphors = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label="Are there clear & distinct metaphors/analogies?")
    setting_specific = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label="Is the setting clear & specific?")
    noun_specific = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label="Are the nouns/characters or items specific?")
    verb_specific = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label="Are the verbs/actions specific?")
    adjective_specific = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label="Are the adjectives/descriptions specific?")
    worldview = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label="Does it communicate a view of how the world works?")
    emi = forms.ChoiceField(choices=EMOTIONAL_IMPACT_INDEX, widget=forms.RadioSelect, label='How did the piece make you feel?')
    favorite_lines = forms.CharField(widget=forms.Textarea(attrs={"class": "mceNoEditor"}), label='What are your favorite lines?')
    comments = forms.CharField(widget=forms.Textarea(attrs={"class": "mceNoEditor"}), label='Additional comments:')

    class Meta:
        model = Feedback
        fields = ['summary', 'progression', 'aural_quality', 'pov_clear', 'style_distinct', 'metaphors', 'setting_specific', 'noun_specific', 'verb_specific', 'adjective_specific', 'worldview', 'emi', 'favorite_lines', 'comments']
