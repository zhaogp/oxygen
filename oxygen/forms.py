from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username or email address',
        label_suffix='',
        widget=TextInput(attrs={'size': '29'})
    )
    password = forms.CharField(
        label='Password', 
        label_suffix='', 
        widget=PasswordInput(attrs={'size': '29'})
    )


class SignupForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True,
        help_text='Usernames may contain <strong>alphanumeric</strong>, <strong>_</strong> and <strong>.</strong> characters',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Confirm your password',
        required=True,
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
        max_length=75,
    )

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['username', 'password', 'email', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

