from django import forms

from ..models import SubjectScreening


# from study_subject_validations.study_subject_validations.form_validators import SubjectScreeningFormValidator


class SubjectModelFormMixin(forms.ModelForm):
    pass


class SubjectScreeningForm(SubjectModelFormMixin):
    # form_validation_cls = SubjectScreeningFormValidator

    class Meta:
        model = SubjectScreening
        fields = '__all__'
