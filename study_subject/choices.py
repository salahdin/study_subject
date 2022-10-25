from edc_constants.constants import OTHER

CITIZEN = 'Citizen'
NON_CITIZEN = 'Non-citizen'
MARRIED_TO_CITIZEN = 'Married to a citizen'

NATIONALITY = (
    (CITIZEN, 'Citizen'),
    (MARRIED_TO_CITIZEN, 'Married to a citizen'),
    (NON_CITIZEN, 'Non-citizen'),
)

LITERACY = (
    ('Literate', 'Literate'),
    ('Illiterate', 'Illiterate'),
)

MARITAL_STATUS_CHOICE = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Cohabiting', 'Cohabiting'),
    ('Widowed', 'Widowed'),
    ('Divorced', 'Divorced'),
    ('Other', 'Other, specify'),
)

HOUSEMATE = (
    ('Alone', 'Alone'),
    ('Partner/Spouse', 'Partner/Spouse'),
    ('Sibling', 'Sibling'),
    (OTHER, 'Other')
)

EMPLOYMENT_TYPE = (
    ('Occasional or Casual employment (piece job)', 'Occasional or Casual employment (piece job)'),
    ('Seasonal employment', 'Seasonal employment'),
    ('Formal wage employment (full-time)', 'Formal wage employment (full-time)'),
    ('Formal wage employment (part-time)', 'Formal wage employment (part-time)'),
    ('Self-employed in agriculture', 'Self-employed in agriculture'),
    ('Self-employed making money (full-time)', 'Self-employed making money (full-time)'),
    ('Self-employed making money (part-time)', 'Self-employed making money (part-time)'),
    ("Don't want to answer", "Don't want to answer"),
    ("Other", "Other")
)

OCCUPATION = (
    ("Farmer (own land)", "Farmer (own land)"),
    ("Farm work on employers land", "Farm work on employers land"),
    ("Domestic worker", "Domestic worker"),
    ("Work in bar/ hotel/ guest house/ entertainment venue", "Work in bar/ hotel/ guest house/ entertainment venue"),
    ("Fishing", "Fishing"),
    ("Mining", "Mining"),
    ("Tourism/game parks", "Tourism/game parks"),
    ("Working in shop / small business", "Working in shop / small business"),
    ("Informal selling", "Informal selling"),
    ("Commercial sex work", "Commercial sex work"),
    ("Transport (trucker/ taxi driver)", "Transport (trucker/ taxi driver)"),
    ("Factory worker", "Factory worker"),
    ("Guard (security company)", "Guard (security company)"),
    ("Police/ Soldier", "Police/ Soldier"),
    ("Clerical and office work", "Clerical and office work"),
    ("Government worker", "Government worker"),
    ("Teacher", "Teacher"),
    ("Health care worker", "Health care worker"),
    ("Other professional", "Other professional"),
    ("Don't want to answer", "Don't want to answer"),
    ("Other", "Other")
)

INCOME_AMOUNT = (
    ("No income", "No income"),
    ("1 - 199 pula", "1 - 199 pula"),
    ("200 - 499 pula", "200 - 499 pula"),
    ("500 - 999 pula", "500 - 999 pula"),
    ("1000 - 4999 pula", "1000 - 4999 pula"),
    ("More than 10,000 pula", "More than 10,000 pula")
)

COMMUNITY_ACTIVITY = (
    ("Very active", "Very active"),
    ("Somewhat active", "Somewhat active"),
    ("Not active at all", "Not active at all"),
    ("Don't want to answer", "Don't want to answer")
)

MAJOR_COMMUNITY_PROBLEMS = (
    (" HIV/AIDS", " HIV/AIDS"),
    ("Schools", "Schools"),
    ("Sewer", "Sewer"),
    ("Unemployment", "Unemployment"),
    ("Roads", "Roads"),
    ("Water", "Water"),
    ("Other, specify", "Other, specify"),
    ("House", "House"),
    ("Malaria", "Malaria")
)

VISIT_INFO_SOURCE = (
    ('Verbal', 'Verbal'),
    ('Other contact w/ subject', 'Other contact with participant (i.e telephone call)'),
    ('Other', 'Other')
)

VISIT_UNSCHEDULED_REASON = (
    ('Cant Make it', " Can't make it "),
    ('Other', 'Other')
)

VISIT_REASON = (
    ('Initial data collection', 'Initial data collection '),
    ('Reason', 'Reason')
)

ID_TYPE = (
    ('country_id', 'Country ID number'),
    ('drivers', 'Driver\'s license'),
    ('passport', 'Passport'),
    ('country_id_rcpt', 'Country ID receipt'),
    (OTHER, 'Other'),
)
