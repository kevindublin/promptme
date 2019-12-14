from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from apps.accounts.models import User, UserPrompt


class SubmitPrompt(forms.ModelForm):
    PUBLIC_OPTION = (
        ('True', 'Public'),
        ('False', 'Private')
    )

    text = forms.CharField(widget=forms.TextInput(attrs={"class": "mceNoEditor add-user-prompt"}), label='')
    public = forms.BooleanField(widget=forms.Select(choices=PUBLIC_OPTION), label='Would you like to share your prompt?', required=False)

    class Meta:
        model = UserPrompt
        fields = ['text', 'public']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'bio',
        )


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
