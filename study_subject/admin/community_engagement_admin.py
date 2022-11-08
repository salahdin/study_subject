from django.contrib import admin
from ..forms import CommunityEngagementForms
from ..models import CommunityEngagement
from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import study_subject_admin


@admin.register(CommunityEngagement, site=study_subject_admin)
class CommunityEngagementAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = CommunityEngagementForms
    fields = (
        "community_activities",
        "election_vote",
        "major_community_problems",
        "neighborhood_help")
    radio_fields = {
        "community_activities": admin.VERTICAL,
        "election_vote": admin.VERTICAL,
        "major_community_problems": admin.VERTICAL,
        "neighborhood_help": admin.VERTICAL}
