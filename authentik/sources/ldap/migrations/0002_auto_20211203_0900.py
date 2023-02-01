# Generated by Django 3.2.9 on 2021-12-03 09:00

import django.db.models.deletion
from django.db import migrations, models

import authentik.sources.ldap.models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_crypto", "0003_certificatekeypair_managed"),
        ("authentik_sources_ldap", "0001_squashed_0012_auto_20210812_1703"),
    ]

    operations = [
        migrations.AddField(
            model_name="ldapsource",
            name="peer_certificate",
            field=models.ForeignKey(
                default=None,
                help_text=(
                    "Optionally verify the LDAP Server's Certificate against the CA Chain in this"
                    " keypair."
                ),
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="authentik_crypto.certificatekeypair",
            ),
        ),
        migrations.AlterField(
            model_name="ldapsource",
            name="server_uri",
            field=models.TextField(
                validators=[
                    authentik.sources.ldap.models.MultiURLValidator(schemes=["ldap", "ldaps"])
                ],
                verbose_name="Server URI",
            ),
        ),
    ]
