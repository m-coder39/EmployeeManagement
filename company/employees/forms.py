from django import forms
from django.contrib.auth.forms import UserCreationForm
from employees.models import CustomUser


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['empid', 'name', 'username', 'deptname', 'salary', 'designation', 'image', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
