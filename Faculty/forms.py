from django import forms
from .models import Faculty

from .validators import file_size_validators


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = {'__all__'}
