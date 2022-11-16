from edc_locator.action_items import SubjectLocatorAction as BaseSubjectLocatorAction

from edc_action_item import site_action_items

SUBJECT_LOCATOR_ACTION = 'submit-study-subject-locator'


# used as reminders to submit subject locator form
class StudySubjectLocatorAction(BaseSubjectLocatorAction):
    name = SUBJECT_LOCATOR_ACTION
    display_name = 'Submit Subject Locator'
    reference_model = 'study_subject.subjectlocator'
    admin_site_name = 'study_subject_admin'


site_action_items.register(StudySubjectLocatorAction)
