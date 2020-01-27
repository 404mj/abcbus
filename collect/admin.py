from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BankUser, PersonalFinance, Dept
from .forms import BankUserChangeForm, BankUserCreationForm

ADDITIONAL_USER_FIELDS = (
    ('自定义关键信息', {'fields': ('dept_id', 'phone',)}),
)


class BankUserAdmin(UserAdmin):
    form = BankUserChangeForm
    model = BankUser
    add_form = BankUserCreationForm
    fieldsets = ADDITIONAL_USER_FIELDS + UserAdmin.fieldsets
    list_display = ['username', 'dept_id', 'phone']
    # add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    # fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS
    # print(fieldsets.__str__())


class DeptAdmin(admin.ModelAdmin):
    list_display = ['dept_id', 'dept_name', 'parent']


admin.site.register(BankUser, BankUserAdmin)
admin.site.register(PersonalFinance)
admin.site.register(Dept, DeptAdmin)
