from edc_identifier.subject_identifier import SubjectIdentifier as StudySubjectIdentifier


class SubjectIdentifier(StudySubjectIdentifier):

    template = '{protocol_number}-0{site_id}{device_id}{sequence}'
