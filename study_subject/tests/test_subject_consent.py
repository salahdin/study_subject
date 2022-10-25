from django.test import TestCase
from ..models.subject_screening import SubjectScreening
from ..models.subject_consent import SubjectConsent
from edc_constants.constants import YES, NO, MALE, OTHER


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
        subject_consent_obj = SubjectConsent.objects.create(
            screening_identifier=self.screening_obj.screening_identifier,
            gender=self.screening_obj.gender,
            partners=2,
            housemate=OTHER
        )
        self.assertIsInstance(subject_consent_obj, SubjectConsent)

    def test_subject_consent_identifier(self):
        subject_consent_obj = SubjectConsent.objects.create(
            screening_identifier=self.screening_obj.screening_identifier,
            gender=self.screening_obj.gender,
            partners=2,
            housemate=OTHER
        )
        self.assertIsNotNone(subject_consent_obj.subject_identifier)
