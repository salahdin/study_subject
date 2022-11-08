from edc_base.sites import SiteModelMixin
from edc_constants.choices import GENDER, YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE, YES, NO
from edc_base.model_mixins import BaseUuidModel
from django.db import models
from edc_base.model_validators import eligible_if_no

from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_search.model_mixins import SearchSlugModelMixin

from ..eligibility import Eligibility
from ..screening_identifier import ScreeningIdentifier


class SubjectScreening(
        UniqueSubjectIdentifierFieldMixin, SiteModelMixin,
        SearchSlugModelMixin, BaseUuidModel):

    eligibility_cls = Eligibility
    identifier_cls = ScreeningIdentifier

    screening_identifier = models.CharField(
        verbose_name="Eligibility Identifier",
        max_length=36,
        unique=True,
        editable=False)

    gender = models.CharField(choices=GENDER,
                              verbose_name="Gender of Participant",
                              max_length=20)

    citizen = models.CharField(
        verbose_name='Is the participant a Botswana citizen? ',
        max_length=3,
        choices=YES_NO,
    )

    legal_marriage = models.CharField(
        verbose_name=(
            'If not a citizen, is the participant '
            'legally married to a Botswana citizen?'),
        max_length=3,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        null=True,
        blank=False,
        help_text="If 'No', participant may not be consented.",
    )

    marriage_certificate = models.CharField(
        verbose_name=(
            '[Interviewer] Has the participant produced the marriage '
            'certificate as proof? '),
        max_length=3,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        null=True,
        help_text='If \'No\', participant may not be consented.',
    )

    marriage_certificate_no = models.CharField(
        verbose_name='What is the marriage certificate number?',
        max_length=9,
        null=True,
        blank=True,
        help_text='e.g. 000/YYYY',
    )

    literacy = models.CharField(
        verbose_name="Is subject literate?",
        max_length=10,
        choices=YES_NO
    )

    witness = models.CharField(
        verbose_name="Is a witness available?",
        max_length=10,
        choices=YES_NO,
        null=True
    )

    is_minor = models.CharField(
        verbose_name="Is a minor( Under 18 )",
        max_length=10,
        choices=YES_NO,
        help_text='If \'YES\', participant may not be consented.',
        validators=[eligible_if_no, ]
    )

    guardian = models.CharField(
        verbose_name="Is a guardian available?",
        max_length=10,
        choices=YES_NO,
        help_text='If \'No\', participant may not be consented.',

    )

    eligible = models.BooleanField()

    def save(self, *args, **kwargs):
        citizenship_status = NO
        if self.citizen == YES:
            citizenship_status = YES
        elif self.legal_marriage == YES:
            if self.marriage_certificate:
                citizenship_status = YES

        eligibility_obj = self.eligibility_cls(citizenship_status=citizenship_status,
                                               literacy=self.literacy,
                                               is_minor=self.is_minor
                                               )
        self.eligible = eligibility_obj.eligible

        if not self.id:
            self.screening_identifier = self.identifier_cls().identifier

        super().save(*args, **kwargs)
