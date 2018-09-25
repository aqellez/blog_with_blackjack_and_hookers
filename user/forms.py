from django import forms
from core.models import Article

class EditorForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body'] 