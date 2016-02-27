from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserForm(forms.Form):
    email = forms.EmailField(required=True)
    helper = FormHelper()
    helper.form_method = 'GET'
    helper.add_input(Submit('search', 'search'))