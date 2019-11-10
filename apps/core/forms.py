from django import forms
from .models import Draft, Feedback


class WriteBox(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        model = Draft
        fields = ['text', ]


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
    setting_specific = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label="Is the setting clear and & specific?")
    noun_specific = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label="Are the nouns/characters or items specific?")
    verb_specific = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label="Are the verbs/actions specific?")
    adjective_specific = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label="Are the adjectives/descriptions specific?")
    worldview = forms.ChoiceField(choices=SURVEY_OPTIONS, widget=forms.RadioSelect, label="Does it communicate how the world works in the microcosm of the piece?")
    emi = forms.ChoiceField(choices=EMOTIONAL_IMPACT_INDEX, widget=forms.RadioSelect, label='How did the piece make you feel?')
    favorite_lines = forms.CharField(widget=forms.Textarea(attrs={"class": "mceNoEditor"}), label='What are your favorite lines?')
    comments = forms.CharField(widget=forms.Textarea(attrs={"class": "mceNoEditor"}), label='Additional comments:')

    class Meta:
        model = Feedback
        fields = ['summary', 'progression', 'aural_quality', 'pov_clear', 'style_distinct', 'metaphors', 'setting_specific', 'noun_specific', 'verb_specific', 'adjective_specific', 'worldview', 'emi', 'favorite_lines', 'comments']
