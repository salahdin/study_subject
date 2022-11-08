from django.contrib import admin
from ..forms import EducationForm
from ..models import Education
from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import study_subject_admin


@admin.register(Education, site=study_subject_admin)
class EducationAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = EducationForm
    fields = (
        "subject_visit",
        "employment",
        "employment_type",
        "occupation",
        "income")
    radio_fields = {
        "employment": admin.VERTICAL,
        "employment_type": admin.VERTICAL,
        "occupation": admin.VERTICAL,
        "income": admin.VERTICAL}
