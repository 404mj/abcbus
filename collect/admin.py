from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BankUser
from .forms import BankUserChangeForm, BankUserCreationForm


class BankUserAdmin(UserAdmin):
    add_form = BankUserCreationForm
    form = BankUserChangeForm
    model = BankUser
    list_display = ['', '']


admin.site.register(BankUser, BankUserAdmin)
