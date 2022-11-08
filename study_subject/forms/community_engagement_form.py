from django import forms
from ..models import CommunityEngagement
from .form_mixins import SubjectModelFormMixin


# from study_subject_validator.study_subject_validator.form_validators import

class CommunityEngagementForms(SubjectModelFormMixin):
    class Meta:
        model = CommunityEngagement
        fields = '__all__'
