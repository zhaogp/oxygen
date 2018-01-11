from django import forms
from django.forms.widgets import PasswordInput, TextInput

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
