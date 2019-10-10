from django import forms
from tinymce import TinyMCE
from .models import Post
from .models import Draft


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = '__all__'


class WriteBox(Draft):
    class Meta(Draft.Meta):
        model = Draft
        fields = (
            'user',
            'text',
            'created',
            'revised',
            'prompt'
        )
        widget = TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
