from django.test import TestCase
from ..models.subject_screening import SubjectScreening
from ..models.subject_consent import SubjectConsent
from edc_constants.constants import YES, NO, MALE, OTHER
from edc_base.utils import get_utcnow

class SubjectConsentTest(TestCase):

    def setUp(self):
        self.screening_obj = SubjectScreening.objects.create(
            gender=MALE,
            citizen=YES,
            legal_marriage=YES,
            marriage_certificate=YES,
            literacy=YES,
            is_minor=NO
        )

    def test_subject_consent(self):

        subject_consent_obj=SubjectConsent.objects.create(
            subject_identifier=None,
            screening_identifier=self.screening_obj.screening_identifier,
            dob=get_utcnow(),
            first_name="John",
            last_name="wamig",
            initials='XX',
            gender=self.screening_obj.gender,
            identity='12315678',
            confirm_identity='12315678',
            identity_type='OMANG',
            is_dob_estimated='-',
            housemate=OTHER,
            partners=2,
        )

        self.assertIsInstance(subject_consent_obj, SubjectConsent)

    def test_subject_consent_identifier(self):
        subject_consent_obj = SubjectConsent.objects.create(
            subject_identifier=None,
            screening_identifier=self.screening_obj.screening_identifier,
            dob=get_utcnow(),
            first_name="John",
            last_name="wamig",
            initials='XX',
            gender=self.screening_obj.gender,
            identity='12315678',
            confirm_identity='12315678',
            identity_type='OMANG',
            is_dob_estimated='-',
            housemate=OTHER,
            partners=2,
        )
        self.assertIsNotNone(subject_consent_obj.subject_identifier)
