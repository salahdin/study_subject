from django import forms
from edc_form_validators import FormValidatorMixin
from ..models import SubjectLocator


# TODO: add validator
class SubjectLocatorForm(forms.ModelForm):
    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectLocator
        fields = '__all__'
