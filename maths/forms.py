from django import forms

class YueForm(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()
