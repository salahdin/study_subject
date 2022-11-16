from django.contrib import admin
from ..models import SubjectConsent
from ..forms import SubjectConsentForm
from ..admin_site import study_subject_admin
from .modeladmin_mixins import ModelAdminMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fields, audit_fieldset_tuple)


@admin.register(SubjectConsent, site=study_subject_admin)
class SubjectConsentAdmin(ModelAdminMixin, admin.ModelAdmin):
    readonly_fields = ('report_datetime',)
    form = SubjectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'screening_identifier',
                'consent_datetime',
                'first_name',
                'last_name',
                'initials',
                'identity_type',
                'identity',
                'confirm_identity',
                'gender',
                'dob',
                'partners',
                'housemate',
            )})
        , audit_fieldset_tuple
    )
