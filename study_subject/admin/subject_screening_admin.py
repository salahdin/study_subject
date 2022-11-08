from django.contrib import admin
from .modeladmin_mixins import ModelAdminMixin
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fields, audit_fieldset_tuple)
from ..admin_site import study_subject_admin
from ..forms import SubjectScreeningForm
from ..models import SubjectScreening


@admin.register(SubjectScreening, site=study_subject_admin)
class SubjectScreeningAdmin(
    ModelAdminMixin, admin.ModelAdmin):
    form = SubjectScreeningForm

    fieldsets = (
        (None, {
            'fields': (
                'gender',
                'citizen',
                'legal_marriage',
                'marriage_certificate',
                'marriage_certificate_no',
                'literacy',
                'witness',
                'is_minor',
                'guardian',
                'eligible'
            )}),
        audit_fieldset_tuple)

    radio_fields = {
        'gender': admin.VERTICAL,
        'citizen': admin.VERTICAL,
        'legal_marriage': admin.VERTICAL,
        'marriage_certificate': admin.VERTICAL,
        'witness': admin.VERTICAL,
        'is_minor': admin.VERTICAL,
        'guardian': admin.VERTICAL,
        'literacy': admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)
