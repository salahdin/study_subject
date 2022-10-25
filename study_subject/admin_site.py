from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Study Subject'
    site_header = 'Study Subject'
    index_title = 'Study Subject'
    site_url = '/study_subject/list/'


study_subject_admin = AdminSite(name='study_subject_admin')
