from django.db import models
from ..choices import COMMUNITY_ACTIVITY, MAJOR_COMMUNITY_PROBLEMS
from edc_constants.choices import YES_NO_NA_DWTA
from .model_mixins import CrfModelMixin


class CommunityEngagement(CrfModelMixin):
    community_activities = models.CharField(
        verbose_name=("How active are you in community activities such as "
                      "burial society, Motshelo, Syndicate, PTA, VDC(Village Development Committee),"
                      " Mophato and development of the community that surrounds you"),
        max_length=100,
        choices=COMMUNITY_ACTIVITY,
    )

    election_vote = models.CharField(
        verbose_name="Did you vote in the last local government election?",
        max_length=100,
        choices=YES_NO_NA_DWTA
    )

    major_community_problems = models.CharField(
        verbose_name="What are the major problems in this neighborhood?",
        max_length=100,
        choices=MAJOR_COMMUNITY_PROBLEMS
    )

    neighborhood_help = models.CharField(
        verbose_name=("If there is a problem in this neighborhood,"
                      " do the adults work together in solving it?"),
        max_length=100,
        choices=YES_NO_NA_DWTA
    )
