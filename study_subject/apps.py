"""
1. Define the app
2. Define the study period.
3. Define timie point
"""
from django.apps import AppConfig as DjangoAppConfig
from edc_appointment.constants import COMPLETE_APPT
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from datetime import datetime
from django.conf import settings

from edc_timepoint import TimepointCollection, Timepoint
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig

from dateutil.tz import gettz


class AppConfig(DjangoAppConfig):
    name = 'study_subject'
    verbose_name = 'Study Subject CRFs'
    admin_site_name = 'study_subject_admin'


if settings.APP_NAME == 'study_subject':
    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP045'
        protocol_name = 'Study'
        protocol_number = '045'
        protocol_title = ''
        study_open_datetime = datetime(
            2010, 5, 2, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2023, 12, 31, 23, 59, 59, tzinfo=gettz('UTC'))


    class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
        timepoints = TimepointCollection(
            timepoints=[
                Timepoint(
                    model='StudySubject.appointment',
                    datetime_field='appt_datetime',
                    status_field='appt_status',
                    closed_status=COMPLETE_APPT),
            ])
