from django import forms
from ..models import CommunityEngagement


# from study_subject_validator.study_subject_validator.form_validators import


# TODO import validators form validator app
class CommunityEngagementForms(forms.ModelForm):
    class Meta:
        model = CommunityEngagement
        fields = '__all__'
