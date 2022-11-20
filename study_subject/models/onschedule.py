from django.contrib.sites.managers import CurrentSiteManager
from django.core.exceptions import ValidationError
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_identifier.managers import SubjectIdentifierManager
from edc_visit_schedule.model_mixins import OnScheduleModelMixin
from edc_consent.model_mixins import RequiresConsentFieldsModelMixin
from django.db import models


class OnSchedule(RequiresConsentFieldsModelMixin, OnScheduleModelMixin, BaseUuidModel):
    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    schedule_name = models.CharField(
        max_length=25,
        null=True,
        blank=True)

    objects = SubjectIdentifierManager()
    history = HistoricalRecords()
    on_site = CurrentSiteManager()
