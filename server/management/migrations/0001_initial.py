# Generated by Django 4.1 on 2022-09-16 07:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("city", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
                ("street", models.CharField(max_length=50)),
                ("house_no", models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresss",
            },
        ),
        migrations.CreateModel(
            name="Campaign",
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
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=255)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
            ],
            options={
                "verbose_name": "Campaign",
                "verbose_name_plural": "Campaigns",
            },
        ),
        migrations.CreateModel(
            name="Company",
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
                (
                    "date_joined",
                    models.DateTimeField(auto_created=True, verbose_name="Date Joined"),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                (
                    "web_url",
                    models.URLField(blank=True, null=True, verbose_name="Web Page"),
                ),
                ("is_active", models.BooleanField(verbose_name="Active")),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.address",
                    ),
                ),
            ],
            options={
                "verbose_name": "Company",
                "verbose_name_plural": "Companies",
            },
        ),
        migrations.CreateModel(
            name="Media",
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
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("media_title", models.CharField(max_length=50)),
                ("media_description", models.TextField(max_length=100)),
                (
                    "media_type",
                    models.SmallIntegerField(
                        choices=[
                            ("1", "Image"),
                            ("2", "Video"),
                            ("3", "Audio"),
                            (
                                "<class 'management.models.Media.MediaType.Meta'>",
                                "Meta",
                            ),
                        ],
                        default="1",
                    ),
                ),
            ],
            options={
                "verbose_name": "Media",
                "verbose_name_plural": "Media",
            },
        ),
        migrations.CreateModel(
            name="Zone",
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
                ("name", models.CharField(max_length=50)),
                (
                    "campaign",
                    models.ForeignKey(
                        help_text="The Compaign that the Zone Belongs to",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.campaign",
                    ),
                ),
            ],
            options={
                "verbose_name": "Zone",
                "verbose_name_plural": "Zones",
            },
        ),
        migrations.CreateModel(
            name="Token",
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
                ("count", models.PositiveBigIntegerField(default=200)),
                ("token_value", models.FloatField()),
                (
                    "offered_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.company",
                    ),
                ),
            ],
            options={
                "verbose_name": "Token",
                "verbose_name_plural": "Tokens",
            },
        ),
        migrations.AddField(
            model_name="campaign",
            name="company",
            field=models.ForeignKey(
                help_text="Company Running the Campaign",
                on_delete=django.db.models.deletion.CASCADE,
                to="management.company",
            ),
        ),
        migrations.CreateModel(
            name="Advertisement",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=255)),
                ("campaigns", models.ManyToManyField(to="management.campaign")),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.company",
                    ),
                ),
                ("zone", models.ManyToManyField(to="management.zone")),
            ],
            options={
                "verbose_name": "Advertisement",
                "verbose_name_plural": "Advertisements",
            },
        ),
    ]
