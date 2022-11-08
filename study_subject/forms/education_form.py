from django import forms
from ..models import Education
from .form_mixins import SubjectModelFormMixin


class EducationForm(SubjectModelFormMixin):
    class Meta:
        model = Education
        fields = '__all__'
