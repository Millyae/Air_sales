from django.db import models
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    phone = forms.IntegerField(label="Phone")

    class Meta:
        model = User
        fields = (
            "email",
            "phone",
            "password1",
            "password2",)


class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user