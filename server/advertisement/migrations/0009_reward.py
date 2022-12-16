# Generated by Django 4.1 on 2022-11-22 02:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0002_delete_token"),
        ("advertisement", "0008_alter_media_share_count_alter_media_view_count"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reward",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_created=True)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("is_valid", models.BooleanField(default=True)),
                ("total", models.PositiveBigIntegerField(default=200)),
                ("per_view_value", models.PositiveSmallIntegerField(default=10)),
                (
                    "assigned_to",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="advertisement.advertisement",
                    ),
                ),
                (
                    "offered_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.company",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reward",
                "verbose_name_plural": "TReward",
            },
        ),
    ]