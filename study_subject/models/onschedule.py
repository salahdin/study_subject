from django.contrib.sites.managers import CurrentSiteManager
from django.core.exceptions import ValidationError
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.managers import SubjectIdentifierManager
from edc_visit_schedule.model_mixins import OnScheduleModelMixin

from .subject_consent import SubjectConsent


class OnSchedule(OnScheduleModelMixin, BaseUuidModel):

    objects = SubjectIdentifierManager()

    history = HistoricalRecords()

    on_site = CurrentSiteManager()
