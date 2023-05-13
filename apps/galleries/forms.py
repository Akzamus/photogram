from django import forms
from .models import Gallery, Picture


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['user', 'name', 'icon']
        widgets = {
            'user': forms.HiddenInput(attrs={'required': False}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
            'icon': forms.TextInput(attrs={'placeholder': 'Enter Icon'})
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].initial = user


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['gallery', 'name', 'description', 'image', 'is_favorite']
        widgets = {
            'gallery': forms.Select(attrs={'placeholder': 'Select Gallery'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter Description'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gallery'].queryset = Gallery.objects.filter(user=user)
