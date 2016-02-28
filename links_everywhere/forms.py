from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class AddLinkForm(forms.Form):
    link = forms.CharField()
    helper = FormHelper()
    helper.form_action = '/links/getmytags'
    helper.form_method = 'GET'
    helper.add_input(Submit('Add link', 'Add link'))


