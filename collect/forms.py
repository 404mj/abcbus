from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import BankUser


class BankUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = BankUser
        fields = ('username', 'dept_id', 'phone')


class BankUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = BankUser
        fields = ('username', 'dept_id', 'phone')
