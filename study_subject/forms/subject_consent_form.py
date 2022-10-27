from django import forms
from edc_consent.modelform_mixins import ConsentModelFormMixin
from ..models import SubjectConsent
from .form_mixins import SubjectModelFormMixin


class SubjectConsentForm(ConsentModelFormMixin, SubjectModelFormMixin,
                         forms.ModelForm):

    # form_validator_cls = SubjectConsentFormValidation

    class Meta:
        model = SubjectConsent
        fields = '__all__'
