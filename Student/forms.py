from django import forms
from .models import StudentDetails
class StudentForm(forms.ModelForm):
    # for field in iter(self.fields):
    #     self.fields[field].widget.attrs.update({
    #         'class': 'form-control'
    #     })

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
            # 'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            # 'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
            # 'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }
        fields = '__all__'