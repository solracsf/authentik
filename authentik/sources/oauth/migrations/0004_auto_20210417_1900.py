# Generated by Django 3.2 on 2021-04-17 19:00
from django.apps.registry import Apps
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def update_empty_urls(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    OAuthSource = apps.get_model("authentik_sources_oauth", "oauthsource")

    db_alias = schema_editor.connection.alias

    for source in OAuthSource.objects.using(db_alias).all():
        changed = False
        if source.access_token_url == "":  # nosec
            source.access_token_url = None
            changed = True
        if source.authorization_url == "":
            source.authorization_url = None
            changed = True
        if source.profile_url == "":
            source.profile_url = None
            changed = True
        if source.request_token_url == "":  # nosec
            source.request_token_url = None
            changed = True

        if changed:
            source.save()


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_sources_oauth", "0003_auto_20210416_0726"),
    ]

    operations = [
        migrations.AlterField(
            model_name="oauthsource",
            name="access_token_url",
            field=models.CharField(
                help_text="URL used by authentik to retrieve tokens.",
                max_length=255,
                null=True,
                verbose_name="Access Token URL",
            ),
        ),
        migrations.AlterField(
            model_name="oauthsource",
            name="authorization_url",
            field=models.CharField(
                help_text="URL the user is redirect to to conest the flow.",
                max_length=255,
                null=True,
                verbose_name="Authorization URL",
            ),
        ),
        migrations.AlterField(
            model_name="oauthsource",
            name="profile_url",
            field=models.CharField(
                help_text="URL used by authentik to get user information.",
                max_length=255,
                null=True,
                verbose_name="Profile URL",
            ),
        ),
        migrations.AlterField(
            model_name="oauthsource",
            name="request_token_url",
            field=models.CharField(
                help_text=(
                    "URL used to request the initial token. This URL is only required for OAuth 1."
                ),
                max_length=255,
                null=True,
                verbose_name="Request Token URL",
            ),
        ),
        migrations.RunPython(update_empty_urls),
    ]
