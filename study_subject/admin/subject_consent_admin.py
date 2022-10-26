from django.contrib import admin
from ..models import SubjectConsent
from ..forms import SubjectConsentForm


@admin.register(SubjectConsent)
class SubjectConsentAdmin(admin.ModelAdmin):
    form = SubjectConsentForm
