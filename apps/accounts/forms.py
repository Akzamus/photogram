from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from PIL import Image

from .models import User


class CustomUserCreationForm(UserCreationForm):
    avatar = forms.ImageField(
        required=True,
        error_messages={
            'required': _('This field is required.'),
        },
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'avatar')

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if not avatar:
            raise forms.ValidationError(_('This field is required.'))

        img = Image.open(avatar)

        width, height = img.size
        if width != height:
            raise forms.ValidationError(_('Avatar should be a square image.'))

        return avatar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': _('Enter Username')})
        self.fields['email'].widget.attrs.update({'placeholder': _('Enter Email Address')})
        self.fields['password1'].widget.attrs.update({'placeholder': _('Enter Password')})
        self.fields['password2'].widget.attrs.update({'placeholder': _('Enter password')})
        self.fields['avatar'].widget.attrs.update({'placeholder': _('Choose Avatar')})
