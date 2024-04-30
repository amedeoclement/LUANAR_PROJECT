
from django import forms
from .models import Gallery



class SearchForm(forms.Form):
    query = forms.CharField(label='Search', widget=forms.TextInput(attrs={'placeholder': 'Type the text here...'}))


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name','images']
    