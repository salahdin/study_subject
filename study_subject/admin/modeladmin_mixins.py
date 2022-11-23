from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites import ModelAdminSiteMixin
from edc_fieldsets import FieldsetsModelAdminMixin
from edc_model_admin import ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin, \
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin, \
    ModelAdminRedirectOnDeleteMixin, FormAsJSONModelAdminMixin
from edc_visit_tracking.modeladmin_mixins import (
    CrfModelAdminMixin as VisitTrackingCrfModelAdminMixin)


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin,
                      ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSiteMixin):
    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


class CrfModelAdminMixin(VisitTrackingCrfModelAdminMixin,
                         ModelAdminMixin,
                         FieldsetsModelAdminMixin,
                         FormAsJSONModelAdminMixin,
                         admin.ModelAdmin):
    post_url_on_delete_name = 'study_subject:subject_dashboard_url'
    instructions = (
        'Please complete the questions below. Required questions are in bold. '
        'When all required questions are complete click SAVE. '
        'Based on your responses, additional questions may be '
        'required or some answers may need to be corrected.')
