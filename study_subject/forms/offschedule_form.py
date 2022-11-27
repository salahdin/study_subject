from ..models import OffSchedule
from django import forms


class OffScheduleForm(forms.ModelForm):
    class Meta:
        fields = '__all__'