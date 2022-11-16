from django.contrib import admin
from ..models import SubjectLocator
from ..forms import SubjectLocatorForm
from ..admin_site import study_subject_admin
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectLocator, site=study_subject_admin)
class SubjectLocatorAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = SubjectLocatorForm
