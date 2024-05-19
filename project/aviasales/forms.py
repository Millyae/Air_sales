from datetime import datetime, date
from django import forms
from django.core.validators import EmailValidator, RegexValidator, MinValueValidator
from .models import *

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'date_of_birth', 'phone_number']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Фамилия Имя Отчество'})
        }
class EmailForm(forms.Form):
    email = forms.CharField(validators=[EmailValidator(message='Invalid email format')])

class NameForm(forms.Form):
    full_name = forms.CharField(validators=[RegexValidator(regex=r'^[А-яа-я\s]+$',message='Onlly Russian letters are allowed')])

class DateOfBirthForm(forms.Form):
    date_of_birth = forms.DateField(input_formats=['%d.%m.%Y'], validators=[MinValueValidator(date(1902, 1, 1))])

class PhoneForm(forms.Form):
    phone_number = forms.CharField(validators=[RegexValidator(regex=r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$', message='Invalid phone number format')])

class PassportForm(forms.Form):
    passport_series = forms.CharField(validators=[RegexValidator(regex=r'^\d{6}$', message='Only 6 digits allowed')])
    passport_number = forms.CharField(validators=[RegexValidator(regex=r'^\d{4}$', message='Only 4 digits allowed')])