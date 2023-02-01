# Generated by Django 3.1.1 on 2020-09-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_stages_prompt", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prompt",
            name="type",
            field=models.CharField(
                choices=[
                    ("text", "Text: Simple Text input"),
                    (
                        "username",
                        (
                            "Username: Same as Text input, but checks for and prevents duplicate"
                            " usernames."
                        ),
                    ),
                    ("email", "Email: Text field with Email type."),
                    (
                        "password",
                        (
                            "Password: Masked input, password is validated against sources."
                            " Policies still have to be applied to this Stage. If two of these are"
                            " used in the same stage, they are ensured to be identical."
                        ),
                    ),
                    ("number", "Number"),
                    ("checkbox", "Checkbox"),
                    ("data", "Date"),
                    ("data-time", "Date Time"),
                    ("separator", "Separator: Static Separator Line"),
                    (
                        "hidden",
                        "Hidden: Hidden field, can be used to insert data into form.",
                    ),
                    ("static", "Static: Static value, displayed as-is."),
                ],
                max_length=100,
            ),
        ),
    ]
