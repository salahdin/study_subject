from django.test import TestCase
from ..models.subject_screening import SubjectScreening
from edc_constants.constants import YES,NO,MALE

class SubjectScreeningTest(TestCase):

    def test_subject_screening(self):
        subject_screening_instance = SubjectScreening.objects.create(
            gender=MALE,
            citizen=YES,
            legal_marriage=YES,
            marriage_certificate=YES,
            literacy=YES,
            is_minor=NO
        )
        # self.assertEqual(str(entry), entry.title)
        self.assertIsInstance(subject_screening_instance, SubjectScreening)

    def test_subject_screening_identifier(self):
        subject_screening_instance = SubjectScreening.objects.create(
            gender=MALE,
            citizen=YES,
            legal_marriage=YES,
            marriage_certificate=YES,
            literacy=YES,
            is_minor=NO
        )
        self.assertIsNotNone(subject_screening_instance.screening_identifier)

    def test_subject_screening_minor(self):
        subject_screening_instance = SubjectScreening.objects.create(
            gender=MALE,
            citizen=YES,
            legal_marriage=YES,
            marriage_certificate=YES,
            literacy=YES,
            is_minor=YES
        )
        self.assertFalse(subject_screening_instance.eligible)
