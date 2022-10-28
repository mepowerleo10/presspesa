# Generated by Django 4.1 on 2022-10-27 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0003_alter_company_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="zone",
            name="campaign",
            field=models.ForeignKey(
                blank=True,
                help_text="The Compaign that the Zone Belongs to",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="management.campaign",
            ),
        ),
    ]
