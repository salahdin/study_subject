from django.contrib import admin
from ..models import SubjectConsent
from ..forms import SubjectConsentForm
from ..admin_site import study_subject_admin


@admin.register(SubjectConsent, site=study_subject_admin)
class SubjectConsentAdmin(admin.ModelAdmin):
    form = SubjectConsentForm
