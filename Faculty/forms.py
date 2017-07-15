from .models import Faculty
from django import forms


class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        fields = { '__all__' }


