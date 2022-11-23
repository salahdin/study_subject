from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin


from ..models import SubjectVisit


class SubjectVisitForm(
    SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):
    # form_validator_cls = VisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = '__all__'
