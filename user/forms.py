from ckeditor.widgets import CKEditorWidget
from django import forms

from core.models import Article


class EditorForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'body', 'hidden', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'body': CKEditorWidget(attrs={'class': 'form-control'}),
            'tags': forms.widgets.SelectMultiple(attrs={'class': 'form-control'}),
        }
