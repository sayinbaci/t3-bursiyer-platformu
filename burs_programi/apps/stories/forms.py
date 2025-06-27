# forms.py
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'surname', 'content', 'profile_image']
        labels = {
            'name': _('Ad'),
            'surname': _('Soyad'),
            'content': _('Yorum'),
            'profile_image': _('Profil Fotoğrafı'),
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': _('Yorumunuzu yazın...')}),
            'profile_image': forms.ClearableFileInput(attrs={
                'class': 'hidden',
                'onchange': 'updateFileName(this)'
            }),
        }
