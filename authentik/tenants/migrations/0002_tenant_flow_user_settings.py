# Generated by Django 4.0.2 on 2022-02-26 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_stages_prompt", "0007_prompt_placeholder_expression"),
        ("authentik_flows", "0021_auto_20211227_2103"),
        ("authentik_tenants", "0001_squashed_0005_tenant_web_certificate"),
    ]

    operations = [
        migrations.AddField(
            model_name="tenant",
            name="flow_user_settings",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="tenant_user_settings",
                to="authentik_flows.flow",
            ),
        ),
    ]