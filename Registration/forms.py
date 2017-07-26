from django import forms

from Configuration.countryConf import countries
from .models import Faculty, Subject, StudentDetails


class StudentForm(forms.ModelForm):
    # for field in iter(self.fields):
    #     self.fields[field].widget.attrs.update({
    #         'class': 'form-control'
    #     })
    current_country = forms.ChoiceField(
        choices=countries
    )
    widgets = {
        'DOB': forms.DateInput(attrs={'class': 'datepicker'})}
    branch = forms.ChoiceField(
        choices=[('Computer', 'Computer'), ('IT', 'IT'), ('EnTC', 'EnTC'), ('Mechanical', 'Mechanical'),
                 ('Civil', 'Civil')])
    admission_type = forms.ChoiceField(
        choices=[('CAP-I', 'CAP-I'), ('CAP-II', 'CAP-II'), ('CAP-III', 'CAP-III'), ('CAPIV', 'CAPIV'),
                 ('Institute Level', 'Institute Level')]
    )
    shift = forms.ChoiceField(
        choices=[('1', 'First-Shift'), ('2', 'Second-Shift')]
    )

    class Meta:
        model = StudentDetails

        widgets = {
            'DOB': forms.DateInput(attrs={'class': 'datepicker'}),
        }
        fields = '__all__'


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        widgets = {
            'DOB': forms.DateInput(attrs={'class': 'datepicker'}),
        }
        fields = '__all__'


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
