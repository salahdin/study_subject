from django.contrib import admin
from ..models import SubjectScreening
from ..forms import SubjectScreeningForm


@admin.register(SubjectScreening)
class SubjectScreeningAdmin(admin.ModelAdmin):
    form = SubjectScreeningForm
