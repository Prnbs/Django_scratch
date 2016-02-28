__author__ = 'prnbs'

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('login', 'login'))
