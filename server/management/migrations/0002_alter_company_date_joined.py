# Generated by Django 4.1 on 2022-10-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="date_joined",
            field=models.DateTimeField(
                auto_created=True, auto_now_add=True, verbose_name="Date Joined"
            ),
        ),
    ]
