from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button


class AddLinkForm(forms.Form):
    link = forms.CharField()
    helper = FormHelper()
    helper.form_action = '/links/getmytags'
    helper.form_method = 'GET'
    helper.add_input(Submit('Add link', 'Add link'))


class SaveLinkForm(forms.Form):
    link = forms.CharField()
    tags = forms.CharField(widget=forms.Textarea)
    helper = FormHelper()
    helper.form_action = '../../links/saveurl/'
    helper.form_method = 'POST'
    helper.add_input(Submit('Save link', 'Save link'))




