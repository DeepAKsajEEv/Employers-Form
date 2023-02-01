from django import forms
from .models import Employee
from django.core.validators import RegexValidator
import json
from django.forms.widgets import SelectDateWidget


def readJson(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        return json.load(fp)

def get_country():
    filepath = './static/data/countries_states.json'
    all_data = readJson(filepath)

    all_countries = [('-----', '---Select a Country---')]

    for x in all_data:
        y = (x['name'], x['name'])
        all_countries.append(y)

    return all_countries


class EmployeeForm(forms.ModelForm):
    number_regex = RegexValidator(regex =r'^[0-9]{10}$',message='Enter valid phone number')
    Name_regex =RegexValidator(regex=r'^[a-zA-ZÀ-ÿ\s]*$',message='Only alpabets are allowed')
    Email_regex =RegexValidator(regex=r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',message='Enter a valid email')
    
    CHOICES = (
        ('Communication','Communication'),
        ('Work under pressure','Work under pressure'),
        ('Decition making','Decition making'),
        ('Time management','Time management'),
        ('Self-motivation','Self-motivation'),
        ('Conflict resolution','Conflict resolution'),
        ('Leadership and adaptability','Leadership and adaptability')
    )

    firstname = forms.CharField(
        label = 'First name',
        min_length=3,max_length=50,
        validators = [Name_regex],
        widget = forms.TextInput(attrs={'placeholder':'Enter First name'})
        )

    lastname = forms.CharField(
        label = 'Last name',
        min_length=3,max_length=50,
        validators = [Name_regex],
        widget = forms.TextInput(attrs={'placeholder':'Enter Last name'})
        )

    email = forms.CharField(label = 'Email',
        min_length=10,
		max_length=50,
		validators = [Email_regex],
		widget = forms.TextInput(attrs={'placeholder':'Enter Email'})
		)
    
    phone_number = forms.CharField(
        label = 'Phone number',
        min_length=9,max_length=50,
        validators = [number_regex],
        widget = forms.TextInput(attrs={'placeholder':'Enter valid phone number without country code'})
        )

    date_of_birth = forms.DateField(widget=SelectDateWidget(years=range(1900, 2100),attrs={'style': 'display: inline-block; width: 10%;'}))

    country = forms.ChoiceField(
        choices = get_country(),
        required = True,
        label='Country',
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_country'}),
        ) 

    professional_skills = forms.MultipleChoiceField(
            label='',
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'my-class'}),
            choices=CHOICES,
            )
      
    photo = forms.ImageField()

    class Meta:
        model = Employee
        exclude = ('state',)