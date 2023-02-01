# Generated by Django 3.2.3 on 2021-05-23 20:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authentik_flows", "0018_oob_flows"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthenticatorDuoStage",
            fields=[
                (
                    "stage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_flows.stage",
                    ),
                ),
                ("client_id", models.TextField()),
                ("client_secret", models.TextField()),
                ("api_hostname", models.TextField()),
                (
                    "configure_flow",
                    models.ForeignKey(
                        blank=True,
                        help_text=(
                            "Flow used by an authenticated user to configure this Stage. If empty,"
                            " user will not be able to configure this stage."
                        ),
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="authentik_flows.flow",
                    ),
                ),
            ],
            options={
                "verbose_name": "Duo Authenticator Setup Stage",
                "verbose_name_plural": "Duo Authenticator Setup Stages",
            },
            bases=("authentik_flows.stage", models.Model),
        ),
        migrations.CreateModel(
            name="DuoDevice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The human-readable name of this device.",
                        max_length=64,
                    ),
                ),
                (
                    "confirmed",
                    models.BooleanField(default=True, help_text="Is this device ready for use?"),
                ),
                ("duo_user_id", models.TextField()),
                (
                    "stage",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authentik_stages_authenticator_duo.authenticatorduostage",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Duo Device",
                "verbose_name_plural": "Duo Devices",
            },
        ),
    ]
