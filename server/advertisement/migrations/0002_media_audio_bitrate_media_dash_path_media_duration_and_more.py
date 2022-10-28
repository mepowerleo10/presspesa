# Generated by Django 4.1 on 2022-10-28 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("advertisement", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="media",
            name="audio_bitrate",
            field=models.CharField(blank=None, default="", max_length=10),
        ),
        migrations.AddField(
            model_name="media",
            name="dash_path",
            field=models.CharField(blank=None, default="", max_length=200),
        ),
        migrations.AddField(
            model_name="media",
            name="duration",
            field=models.FloatField(blank=None, default=0.0),
        ),
        migrations.AddField(
            model_name="media",
            name="format",
            field=models.CharField(blank=None, default="", max_length=50),
        ),
        migrations.AddField(
            model_name="media",
            name="height",
            field=models.CharField(blank=None, default="", max_length=50),
        ),
        migrations.AddField(
            model_name="media",
            name="is_done_processing",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="media",
            name="overall_bitrate",
            field=models.CharField(blank=None, default="", max_length=200),
        ),
        migrations.AddField(
            model_name="media",
            name="size",
            field=models.FloatField(blank=None, default=0.0),
        ),
        migrations.AddField(
            model_name="media",
            name="video_bitrate",
            field=models.CharField(blank=None, default="", max_length=10),
        ),
        migrations.AddField(
            model_name="media",
            name="width",
            field=models.CharField(blank=None, default="", max_length=50),
        ),
    ]
