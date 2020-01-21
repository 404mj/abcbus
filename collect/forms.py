from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import BankUser


class BankUserCreationForm(UserCreationForm):
    class Meta:
        model = BankUser
        fields = ()


class BankUserChangeForm(UserChangeForm):
    class Meta:
        model = BankUser
        fields = ()
