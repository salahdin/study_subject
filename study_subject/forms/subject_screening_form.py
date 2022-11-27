from django import forms

from ..models import SubjectScreening


class SubjectModelFormMixin(forms.ModelForm):
    pass


class SubjectScreeningForm(SubjectModelFormMixin):
    # form_validation_cls = SubjectScreeningFormValidator
    screening_identifier = forms.CharField(
        label='Screening Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectScreening
        fields = '__all__'
