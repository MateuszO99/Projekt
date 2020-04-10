from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = 'Dodaj komentarz:'

    class Meta:
        model = Comment
        fields = ['content']
