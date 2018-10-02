from django import forms
from core.models import Article
from ckeditor.widgets import CKEditorWidget


class EditorForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'body': CKEditorWidget(attrs={'class': 'form-control'}),
        } 
        