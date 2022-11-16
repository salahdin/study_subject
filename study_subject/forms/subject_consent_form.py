from django import forms
from edc_consent.modelform_mixins import ConsentModelFormMixin
from ..models import SubjectConsent
from .form_mixins import SubjectModelFormMixin
from edc_constants.choices import IDENTITY_TYPE


# TODO: add validator
class SubjectConsentForm(ConsentModelFormMixin, SubjectModelFormMixin):
    # form_validator_cls = SubjectConsentFormValidation
    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    identity_type = forms.CharField(
        label='What type of identity number is this?',
        widget=forms.RadioSelect(choices=list(IDENTITY_TYPE)))

    class Meta:
        model = SubjectConsent
        fields = '__all__'
