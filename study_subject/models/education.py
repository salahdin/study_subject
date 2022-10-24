from django.db import models
from ..choices import EMPLOYMENT_TYPE, OCCUPATION, INCOME_AMOUNT
from edc_constants.choices import YES_NO
from .model_mixins import CrfModelMixin


class Education(CrfModelMixin):
    employment = models.CharField(
        verbose_name="Are you currently working?",
        max_length=10,
        choices=YES_NO,
    )

    employment_type = models.CharField(
        verbose_name="In your main job what type of work do you do?",
        max_length=100,
        choices=EMPLOYMENT_TYPE,
    )

    occupation = models.CharField(
        verbose_name="occupation type",
        max_length=250,
        help_text="choose the option that Describe the work that you do or did in your most recent job."
                  " If you have more than one profession, choose the one you spend the most time doing.",
        choices=OCCUPATION

    )

    income = models.CharField(
        verbose_name="In the past month, how much money did you earn from work you did or received in payment?",
        max_length=150,
        choices=INCOME_AMOUNT
    )
