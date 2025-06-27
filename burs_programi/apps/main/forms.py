# apps/main/forms.py

from django import forms
from .models import Application
from ckeditor.widgets import CKEditorWidget
from .models import ScholarshipProgram

PROJECT_CHOICES = [
    ('teknofest', 'Teknofest'),
    ('deneyap', 'Deneyap'),
    ('bilim_turkiye', 'Bilim Türkiye'),
    ('t3ai', 'T3AI'),
]

class ApplicationForm(forms.ModelForm):
    important_project_order = forms.MultipleChoiceField(
        choices=PROJECT_CHOICES,
        widget=forms.SelectMultiple(attrs={'class': 'form-multiselect'})
    )

    class Meta:
        model = Application
        fields = [
            'full_name', 'identity_number', 'phone', 'email', 'address',
            'student_certificate', 'motivation', 'important_project_order'
        ]
        widgets = {
            'motivation': forms.Textarea(attrs={'rows': 5}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class ScholarshipProgramAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = ScholarshipProgram
        fields = '__all__'

