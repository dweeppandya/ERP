from django import forms

from .models import Faculty, Subject, StudentDetails


class StudentForm(forms.ModelForm):
    # for field in iter(self.fields):
    #     self.fields[field].widget.attrs.update({
    #         'class': 'form-control'
    #     })
    country = forms.ChoiceField(
        choices=[('India', 'India'),
                 ('Afghanistan', 'Afghanistan'),
                 ('Albania', 'Albania'),
                 ('Algeria', 'Algeria'),
                 ('Andorra', 'Andorra'),
                 ('Angola', 'Angola'),
                 ('Antigua and Barbuda', 'Antigua and Barbuda'),
                 ('Argentina', 'Argentina'),
                 ('Armenia', 'Armenia'),
                 ('Australia', 'Australia'),
                 ('Ashmore and Cartier Islands', 'Ashmore and Cartier Islands'),
                 ('Australian Antarctic Territory', 'Australian Antarctic Territory'),
                 ('Christmas Island', 'Christmas Island'),
                 ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
                 ('Coral Sea Islands Territory', 'Coral Sea Islands Territory'),
                 ('Heard Island and McDonald Islands', 'Heard Island and McDonald Islands'),
                 ('Norfolk Island', 'Norfolk Island'),
                 ('Austria', 'Austria'),
                 ('Azerbaijan', 'Azerbaijan'),
                 ('Bahamas', 'Bahamas'),
                 ('Bahrain', 'Bahrain'),
                 ('Bangladesh', 'Bangladesh'),
                 ('Barbados', 'Barbados'),
                 ('Belarus', 'Belarus'),
                 ('Belgium', 'Belgium'),
                 ('Belize', 'Belize'),
                 ('Benin', 'Benin'),
                 ('Bhutan', 'Bhutan'),
                 ('Bolivia', 'Bolivia'),
                 ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
                 ('Federation of Bosnia and Herzegovina', 'Federation of Bosnia and Herzegovina'),
                 ('Republika Srpska', 'Republika Srpska'),
                 ('Botswana', 'Botswana'),
                 ('Brazil', 'Brazil'),
                 ('Brunei', 'Brunei'),
                 ('Bulgaria', 'Bulgaria'),
                 ('Burkina Faso', 'Burkina Faso'),
                 ('Burma', 'Burma'),
                 ('Burundi', 'Burundi'),
                 ('Cambodia', 'Cambodia'),
                 ('Cameroon', 'Cameroon'),
                 ('Canada', 'Canada'),
                 ('Cape Verde', 'Cape Verde'),
                 ('Central African Republic', 'Central African Republic'),
                 ('Chad', 'Chad'),
                 ('Chile', 'Chile'),
                 ('China', 'China'),
                 ('Hong Kong', 'Hong Kong'),
                 ('Macau', 'Macau'),
                 ('Colombia', 'Colombia'),
                 ('Comoros', 'Comoros'),
                 ('Congo', 'Congo'),
                 (' Democratic Republic of the', ' Democratic Republic of the'),
                 ('Congo', 'Congo'),
                 (' Republic of the', ' Republic of the'),
                 ('Costa Rica', 'Costa Rica'),
                 ('Croatia', 'Croatia'),
                 ('Cuba', 'Cuba'),
                 ('Cyprus', 'Cyprus'),
                 ('Czech Republic', 'Czech Republic'),
                 ('Denmark', 'Denmark'),
                 ('Faroe Islands', 'Faroe Islands'),
                 ('Greenland', 'Greenland'),
                 ('Djibouti', 'Djibouti'),
                 ('Dominica', 'Dominica'),
                 ('Dominican Republic', 'Dominican Republic'),
                 ('East Timor', 'East Timor'),
                 ('Ecuador', 'Ecuador'),
                 ('Egypt', 'Egypt'),
                 ('El Salvador', 'El Salvador'),
                 ('Equatorial Guinea', 'Equatorial Guinea'),
                 ('Eritrea', 'Eritrea'),
                 ('Estonia', 'Estonia'),
                 ('Ethiopia', 'Ethiopia'),
                 ('Fiji', 'Fiji'),
                 ('Finland', 'Finland'),
                 ('Åland', 'Åland'),
                 ('France', 'France'),
                 ('Clipperton Island', 'Clipperton Island'),
                 ('French Polynesia', 'French Polynesia'),
                 ('New Caledonia', 'New Caledonia'),
                 ('Saint Barthélemy', 'Saint Barthélemy'),
                 ('Saint Martin', 'Saint Martin'),
                 ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'),
                 ('Wallis and Futuna', 'Wallis and Futuna'),
                 ('French Southern and Antarctic Lands', 'French Southern and Antarctic Lands'),
                 ('Gabon', 'Gabon'),
                 ('Gambia', 'Gambia'),
                 (' The', ' The'),
                 ('Georgia', 'Georgia'),
                 ('Germany', 'Germany'),
                 ('Ghana', 'Ghana'),
                 ('Greece', 'Greece'),
                 ('Grenada', 'Grenada'),
                 ('Guatemala', 'Guatemala'),
                 ('Guinea', 'Guinea'),
                 ('Guinea-Bissau', 'Guinea-Bissau'),
                 ('Guyana', 'Guyana'),
                 ('Haiti', 'Haiti'),
                 ('Honduras', 'Honduras'),
                 ('Hungary', 'Hungary'),
                 ('Iceland', 'Iceland'),
                 ('Indonesia', 'Indonesia'),
                 ('Iran', 'Iran'),
                 ('Iraq', 'Iraq'),
                 ('Ireland', 'Ireland'),
                 ('Israel', 'Israel'),
                 ('Italy', 'Italy'),
                 ('Ivory Coast', 'Ivory Coast'),
                 ('Jamaica', 'Jamaica'),
                 ('Japan', 'Japan'),
                 ('Jordan', 'Jordan'),
                 ('Kazakhstan', 'Kazakhstan'),
                 ('Kenya', 'Kenya'),
                 ('Kiribati', 'Kiribati'),
                 ('Korea', 'Korea'),
                 (' North', ' North'),
                 ('Korea', 'Korea'),
                 (' South', ' South'),
                 ('Kuwait', 'Kuwait'),
                 ('Kyrgyzstan', 'Kyrgyzstan'),
                 ('Laos', 'Laos'),
                 ('Latvia', 'Latvia'),
                 ('Lebanon', 'Lebanon'),
                 ('Lesotho', 'Lesotho'),
                 ('Liberia', 'Liberia'),
                 ('Libya', 'Libya'),
                 ('Cyrenaica', 'Cyrenaica'),
                 ('Liechtenstein', 'Liechtenstein'),
                 ('Lithuania', 'Lithuania'),
                 ('Luxembourg', 'Luxembourg'),
                 ('Macedonia', 'Macedonia'),
                 ('Madagascar', 'Madagascar'),
                 ('Malawi', 'Malawi'),
                 ('Malaysia', 'Malaysia'),
                 ('Maldives', 'Maldives'),
                 ('Mali', 'Mali'),
                 ('Malta', 'Malta'),
                 ('Marshall Islands', 'Marshall Islands'),
                 ('Mauritania', 'Mauritania'),
                 ('Mauritius', 'Mauritius'),
                 ('Mexico', 'Mexico'),
                 ('Micronesia', 'Micronesia'),
                 ('Federated States of', 'Federated States of'),
                 ('Moldova', 'Moldova'),
                 ('Monaco', 'Monaco'),
                 ('Mongolia', 'Mongolia'),
                 ('Montenegro', 'Montenegro'),
                 ('Morocco', 'Morocco'),
                 ('Mozambique', 'Mozambique'),
                 ('Namibia', 'Namibia'),
                 ('Nauru', 'Nauru'),
                 ('Nepal', 'Nepal'),
                 ('Netherlands', 'Netherlands'),
                 ('Netherlands', 'Netherlands'),
                 ('Aruba', 'Aruba'),
                 ('Curaçao', 'Curaçao'),
                 ('Sint Maarten', 'Sint Maarten'),
                 ('New Zealand', 'New Zealand'),
                 ('Ross Dependency', 'Ross Dependency'),
                 ('Tokelau', 'Tokelau'),
                 ('Cook Islands', 'Cook Islands'),
                 ('Niue', 'Niue'),
                 ('Nicaragua', 'Nicaragua'),
                 ('Niger', 'Niger'),
                 ('Nigeria', 'Nigeria'),
                 ('Norway', 'Norway'),
                 ('Oman', 'Oman'),
                 ('Pakistan', 'Pakistan'),
                 ('Azad Kashmir', 'Azad Kashmir'),
                 ('Gilgit–Baltistan', 'Gilgit–Baltistan'),
                 ('Palau', 'Palau'),
                 ('Palestine', 'Palestine'),
                 ('Panama', 'Panama'),
                 ('Papua New Guinea', 'Papua New Guinea'),
                 ('Paraguay', 'Paraguay'),
                 ('Peru', 'Peru'),
                 ('Philippines', 'Philippines'),
                 ('Poland', 'Poland'),
                 ('Portugal', 'Portugal'),
                 ('Qatar', 'Qatar'),
                 ('Romania', 'Romania'),
                 ('Russia', 'Russia'),
                 ('Rwanda', 'Rwanda'),
                 ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
                 ('Saint Lucia', 'Saint Lucia'),
                 ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
                 ('Samoa', 'Samoa'),
                 ('San Marino', 'San Marino'),
                 ('São Tomé and Príncipe', 'São Tomé and Príncipe'),
                 ('Saudi Arabia', 'Saudi Arabia'),
                 ('Senegal', 'Senegal'),
                 ('Serbia', 'Serbia'),
                 ('Seychelles', 'Seychelles'),
                 ('Sierra Leone', 'Sierra Leone'),
                 ('Singapore', 'Singapore'),
                 ('Slovakia', 'Slovakia'),
                 ('Slovenia', 'Slovenia'),
                 ('Solomon Islands', 'Solomon Islands'),
                 ('Somalia', 'Somalia'),
                 ('South Africa', 'South Africa'),
                 ('South Sudan', 'South Sudan'),
                 ('Spain', 'Spain'),
                 ('Sri Lanka', 'Sri Lanka'),
                 ('Sudan', 'Sudan'),
                 ('Suriname', 'Suriname'),
                 ('Swaziland', 'Swaziland'),
                 ('Sweden', 'Sweden'),
                 ('Switzerland', 'Switzerland'),
                 ('Syria', 'Syria'),
                 ('Tajikistan', 'Tajikistan'),
                 ('Tanzania', 'Tanzania'),
                 ('Thailand', 'Thailand'),
                 ('Togo', 'Togo'),
                 ('Tonga', 'Tonga'),
                 ('Trinidad and Tobago', 'Trinidad and Tobago'),
                 ('Tunisia', 'Tunisia'),
                 ('Turkey', 'Turkey'),
                 ('Turkmenistan', 'Turkmenistan'),
                 ('Tuvalu', 'Tuvalu'),
                 ('Uganda', 'Uganda'),
                 ('Ukraine', 'Ukraine'),
                 ('United Arab Emirates', 'United Arab Emirates'),
                 ('United Kingdom', 'United Kingdom'),
                 ('Akrotiri and Dhekelia', 'Akrotiri and Dhekelia'),
                 ('Anguilla', 'Anguilla'),
                 ('Bermuda', 'Bermuda'),
                 ('British Indian Ocean Territory', 'British Indian Ocean Territory'),
                 ('British Virgin Islands', 'British Virgin Islands'),
                 ('Cayman Islands', 'Cayman Islands'),
                 ('Falkland Islands', 'Falkland Islands'),
                 ('Gibraltar', 'Gibraltar'),
                 ('Montserrat', 'Montserrat'),
                 ('Pitcairn Islands', 'Pitcairn Islands'),
                 ('Saint Helena', 'Saint Helena'),
                 (' Ascension and Tristan da Cunha', ' Ascension and Tristan da Cunha'),
                 ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'),
                 ('Turks and Caicos Islands', 'Turks and Caicos Islands'),
                 ('British Antarctic Territory', 'British Antarctic Territory'),
                 ('Guernsey', 'Guernsey'),
                 ('Alderney', 'Alderney'),
                 ('Herm', 'Herm'),
                 ('Sark', 'Sark'),
                 ('Isle of Man', 'Isle of Man'),
                 ('Jersey', 'Jersey'),
                 ('United States', 'United States'),
                 ('American Samoa', 'American Samoa'),
                 ('Guam', 'Guam'),
                 ('Northern Mariana Islands', 'Northern Mariana Islands'),
                 ('Puerto Rico', 'Puerto Rico'),
                 ('U.S. Virgin Islands', 'U.S. Virgin Islands'),
                 ('Marshall Islands', 'Marshall Islands'),
                 ('Micronesia', 'Micronesia'),
                 ('Palau', 'Palau'),
                 ('Uruguay', 'Uruguay'),
                 ('Uzbekistan', 'Uzbekistan'),
                 ('Vanuatu', 'Vanuatu'),
                 ('Vatican City', 'Vatican City'),
                 ('Venezuela', 'Venezuela'),
                 ('Vietnam', 'Vietnam'),
                 ('Yemen', 'Yemen'),
                 ('Zambia', 'Zambia'),
                 ('Zimbabwe', 'Zimbabwe'),
                 ('Abkhazia', 'Abkhazia'),
                 ('Cook Islands', 'Cook Islands'),
                 ('Kosovo', 'Kosovo'),
                 ('Nagorno-Karabakh', 'Nagorno-Karabakh'),
                 ('Niue', 'Niue'),
                 ('Northern Cyprus', 'Northern Cyprus'),
                 ('Sahrawi Arab Democratic Republic', 'Sahrawi Arab Democratic Republic'),
                 ('Somaliland', 'Somaliland'),
                 ('South Ossetia', 'South Ossetia'),
                 ('Taiwan', 'Taiwan'),
                 ('Transnistria', 'Transnistria')]
    )

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


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
