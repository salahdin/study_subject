from django.contrib import admin
from ..models import OffSchedule
from ..forms import OffScheduleForm
from ..admin_site import study_subject_admin
from .modeladmin_mixins import ModelAdminMixin


@admin.register(OffSchedule, site=study_subject_admin)
class OffScheduleAdmin(ModelAdminMixin,admin.ModelAdmin):
    form = OffScheduleForm
