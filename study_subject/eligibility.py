from edc_constants.constants import YES
import datetime


class CitizenshipEvaluator:

    def __init__(self, citizen=None, ):
        self.eligible = None
        if citizen == YES:
            self.eligible = True
        else:
            self.eligible = False


class AgeEvaluator:

    def __init__(self, is_minor=None, ):
        self.eligible = None
        if is_minor == YES:
            self.eligible = True
        else:
            self.eligible = False


class LiteracyEvaluator:

    def __init__(self, literacy):
        self.eligible = None
        if literacy == YES:
            self.eligible = True
        else:
            self.eligible = False


class Eligibility:

    def __init__(self, citizenship_status=None, literacy=None, is_minor=None):
        self.citizenship = CitizenshipEvaluator(citizen=citizenship_status)
        self.literacy = LiteracyEvaluator(literacy=literacy)
        self.is_minor = AgeEvaluator(is_minor=is_minor)
        self.criteria = dict(
            citizenship=self.citizenship.eligible,
            is_minor=self.is_minor.eligible,
            literecy=self.literacy.eligible
        )
        self.eligible = all(self.criteria.values())
