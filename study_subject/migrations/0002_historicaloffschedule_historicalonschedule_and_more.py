# Generated by Django 4.1.2 on 2022-11-20 19:14

import _socket
from django.conf import settings
import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.model_validators.date
import edc_base.sites.managers
import edc_base.utils
import edc_identifier.managers
import edc_model.validators.date
import edc_model_fields.fields.date_estimated
import edc_protocol.validators
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_appointment", "0016_alter_historicalappointment_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sites", "0002_alter_domain_unique"),
        ("study_subject", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalOffSchedule",
            fields=[
                (
                    "created",
                    models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
                ),
                (
                    "user_created",
                    edc_base.model_fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    edc_base.model_fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    edc_base.model_fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    edc_base.model_fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                ("subject_identifier", models.CharField(db_index=True, max_length=50)),
                ("report_datetime", models.DateTimeField(editable=False)),
                (
                    "offschedule_datetime",
                    models.DateTimeField(
                        default=edc_base.utils.get_utcnow,
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_base.model_validators.date.datetime_not_future,
                        ],
                        verbose_name="Date and time subject taken off schedule",
                    ),
                ),
                (
                    "schedule_name",
                    models.CharField(blank=True, max_length=25, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(blank=True, max_length=2, null=True),
                ),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_id",
                    edc_base.model_fields.uuid_auto_field.UUIDAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "verbose_name": "historical off schedule",
                "verbose_name_plural": "historical off schedules",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalOnSchedule",
            fields=[
                (
                    "created",
                    models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
                ),
                (
                    "user_created",
                    edc_base.model_fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    edc_base.model_fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    edc_base.model_fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    edc_base.model_fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                ("report_datetime", models.DateTimeField(editable=False)),
                (
                    "onschedule_datetime",
                    models.DateTimeField(
                        default=edc_base.utils.get_utcnow,
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_base.model_validators.date.datetime_not_future,
                        ],
                    ),
                ),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "subject_identifier",
                    models.CharField(max_length=50, verbose_name="Subject Identifier"),
                ),
                (
                    "schedule_name",
                    models.CharField(blank=True, max_length=25, null=True),
                ),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_id",
                    edc_base.model_fields.uuid_auto_field.UUIDAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
            ],
            options={
                "verbose_name": "historical on schedule",
                "verbose_name_plural": "historical on schedules",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="OffSchedule",
            fields=[
                (
                    "created",
                    models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
                ),
                (
                    "user_created",
                    edc_base.model_fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    edc_base.model_fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    edc_base.model_fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    edc_base.model_fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("subject_identifier", models.CharField(max_length=50, unique=True)),
                ("report_datetime", models.DateTimeField(editable=False)),
                (
                    "offschedule_datetime",
                    models.DateTimeField(
                        default=edc_base.utils.get_utcnow,
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_base.model_validators.date.datetime_not_future,
                        ],
                        verbose_name="Date and time subject taken off schedule",
                    ),
                ),
                (
                    "schedule_name",
                    models.CharField(blank=True, max_length=25, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(blank=True, max_length=2, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", edc_identifier.managers.SubjectIdentifierManager()),
                ("on_site", edc_base.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name="OnSchedule",
            fields=[
                (
                    "created",
                    models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow),
                ),
                (
                    "user_created",
                    edc_base.model_fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    edc_base.model_fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    edc_base.model_fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    edc_base.model_fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("report_datetime", models.DateTimeField(editable=False)),
                (
                    "onschedule_datetime",
                    models.DateTimeField(
                        default=edc_base.utils.get_utcnow,
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_base.model_validators.date.datetime_not_future,
                        ],
                    ),
                ),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "subject_identifier",
                    models.CharField(max_length=50, verbose_name="Subject Identifier"),
                ),
                (
                    "schedule_name",
                    models.CharField(blank=True, max_length=25, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", edc_identifier.managers.SubjectIdentifierManager()),
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name="communityengagement",
            name="consent_model",
            field=models.CharField(editable=False, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="communityengagement",
            name="consent_version",
            field=models.CharField(editable=False, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="education",
            name="consent_model",
            field=models.CharField(editable=False, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="education",
            name="consent_version",
            field=models.CharField(editable=False, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="historicalsubjectvisit",
            name="consent_model",
            field=models.CharField(editable=False, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="historicalsubjectvisit",
            name="consent_version",
            field=models.CharField(editable=False, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="subjectvisit",
            name="consent_model",
            field=models.CharField(editable=False, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="subjectvisit",
            name="consent_version",
            field=models.CharField(editable=False, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalappointment",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="consent_datetime",
            field=models.DateTimeField(
                validators=[
                    edc_protocol.validators.datetime_not_before_study_start,
                    edc_model.validators.date.datetime_not_future,
                ],
                verbose_name="Consent date and time",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="identity_type",
            field=models.CharField(
                choices=[
                    ("country_id", "Country ID number"),
                    ("drivers", "Driver's license"),
                    ("passport", "Passport"),
                    ("hospital_no", "Hospital number"),
                    ("country_id_rcpt", "Country ID receipt"),
                    ("OTHER", "Other"),
                ],
                max_length=25,
                verbose_name="What type of identity number is this?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="is_dob_estimated",
            field=edc_model_fields.fields.date_estimated.IsDateEstimatedField(
                choices=[
                    ("-", "No"),
                    ("D", "Yes, estimated the Day"),
                    ("MD", "Yes, estimated Month and Day"),
                    ("YMD", "Yes, estimated Year, Month and Day"),
                ],
                help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                max_length=25,
                null=True,
                verbose_name="Is date of birth estimated?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="subject_identifier",
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalsubjectlocator",
            name="subject_identifier",
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="appointment",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="edc_appointment.appointment",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectvisit",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="subjectconsent",
            name="consent_datetime",
            field=models.DateTimeField(
                validators=[
                    edc_protocol.validators.datetime_not_before_study_start,
                    edc_model.validators.date.datetime_not_future,
                ],
                verbose_name="Consent date and time",
            ),
        ),
        migrations.AlterField(
            model_name="subjectconsent",
            name="identity_type",
            field=models.CharField(
                choices=[
                    ("country_id", "Country ID number"),
                    ("drivers", "Driver's license"),
                    ("passport", "Passport"),
                    ("hospital_no", "Hospital number"),
                    ("country_id_rcpt", "Country ID receipt"),
                    ("OTHER", "Other"),
                ],
                max_length=25,
                verbose_name="What type of identity number is this?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectconsent",
            name="is_dob_estimated",
            field=edc_model_fields.fields.date_estimated.IsDateEstimatedField(
                choices=[
                    ("-", "No"),
                    ("D", "Yes, estimated the Day"),
                    ("MD", "Yes, estimated Month and Day"),
                    ("YMD", "Yes, estimated Year, Month and Day"),
                ],
                help_text="If the exact date is not known, please indicate which part of the date is estimated.",
                max_length=25,
                null=True,
                verbose_name="Is date of birth estimated?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectconsent",
            name="subject_identifier",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="subjectlocator",
            name="subject_identifier",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="subject_identifier",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="appointment",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                to="edc_appointment.appointment",
            ),
        ),
        migrations.AlterField(
            model_name="subjectvisit",
            name="subject_identifier",
            field=models.CharField(max_length=50),
        ),
        migrations.AddIndex(
            model_name="subjectconsent",
            index=models.Index(
                fields=[
                    "subject_identifier",
                    "first_name",
                    "dob",
                    "initials",
                    "version",
                ],
                name="study_subje_subject_eb6e71_idx",
            ),
        ),
        migrations.AddField(
            model_name="onschedule",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="sites.site",
            ),
        ),
        migrations.AddField(
            model_name="offschedule",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="sites.site",
            ),
        ),
        migrations.AddField(
            model_name="historicalonschedule",
            name="history_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="historicalonschedule",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.site",
            ),
        ),
        migrations.AddField(
            model_name="historicaloffschedule",
            name="history_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="historicaloffschedule",
            name="site",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="sites.site",
            ),
        ),
    ]
