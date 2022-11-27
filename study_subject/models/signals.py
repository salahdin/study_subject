from django.db.models.signals import post_save
from django.dispatch import receiver

from .subject_consent import SubjectConsent
from .subject_screening import SubjectScreening
from edc_visit_schedule.site_visit_schedules import site_visit_schedules


@receiver(post_save, weak=False, sender=SubjectConsent,
          dispatch_uid='subject_consent_on_post_save')
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    if not raw:
        if created:
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                onschedule_model='study_subject.onschedule')

            subject_screening_obj = SubjectScreening.objects.get(
                screening_identifier=instance.screening_identifier
            )
            subject_screening_obj.subject_identifier = instance.subject_identifier
            subject_screening_obj.save()

            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.report_datetime)
