from django.core.exceptions import ImproperlyConfigured
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
#from edc_consent.field_mixins import VulnerabilityFieldsMixin, SampleCollectionFieldsMixin, IdentityFieldsMixin, \
#    ReviewFieldsMixin, CitizenFieldsMixin, PersonalFieldsMixin
#from edc_consent.model_mixins import ConsentModelMixin
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin, NonUniqueSubjectIdentifierModelMixin
from django.db import models
from ..choices import HOUSEMATE
from edc_constants.choices import GENDER
from edc_base.constants import DEFAULT_BASE_FIELDS
from edc_consent.managers import ConsentManager as SubjectConsentManager

from edc_search.model_mixins import SearchSlugManager
from edc_base.model_managers import HistoricalRecords
from ..subject_identifier import SubjectIdentifier
from .model_mixins import SearchSlugModelMixin


class SubjectConsent(
    SiteModelMixin,
    NonUniqueSubjectIdentifierModelMixin, SearchSlugModelMixin, BaseUuidModel):
    screening_identifier = models.CharField(
        verbose_name='Screening identifier',
        null=True,
        blank=True,
        max_length=50)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER,
        max_length=1,
        null=True,

    )

    partners = models.IntegerField(
        verbose_name="How many wives does the participant have",
    )

    housemate = models.CharField(
        verbose_name="Who do you live with?",
        choices=HOUSEMATE,
        max_length=50,
        null=True,

    )

    is_signed = models.BooleanField(default=False, editable=False)

    consent = SubjectConsentManager()

    objects = SubjectConsentManager()

    history = HistoricalRecords()

    # on_site = CurrentSiteManager()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def save(self, *args, **kwargs):
        self.subject_type = 'subject'
        super().save(*args, **kwargs)

    def natural_key(self):
        return self.subject_identifier, self.version,

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend(['identity', 'screening_identifier',
                       'first_name', 'last_name'])
        return fields

    def make_new_identifier(self):
        """Returns a new and unique identifier.
        Override this if needed.
        """
        subject_identifier = SubjectIdentifier(
            identifier_type='subject',
            requesting_model=self._meta.label_lower,
            site=self.site)
        return subject_identifier.identifier

    """class Meta(ConsentModelMixin.Meta):
        app_label = 'study_subject'
        get_latest_by = 'consent_datetime'
        unique_together = (('subject_identifier', 'version'),
                           ('first_name', 'dob', 'initials', 'version'))
        ordering = ('-created',)"""