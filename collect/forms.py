from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import BankUser, PersonalFinance


class BankUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = BankUser
        fields = ('username', 'dept_id', 'phone')


class BankUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = BankUser
        fields = ('username', 'dept_id', 'phone')


# 个金模型表单
class PersonalFinanceForm(ModelForm):
    class Meta:
        model = PersonalFinance
        fields = ['large_deposit', 'precious_metal', 'found', 'memo']
