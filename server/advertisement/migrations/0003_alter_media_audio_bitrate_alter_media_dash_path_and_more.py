# Generated by Django 4.1 on 2022-10-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "advertisement",
            "0002_media_audio_bitrate_media_dash_path_media_duration_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="media",
            name="audio_bitrate",
            field=models.CharField(blank=True, default="", max_length=10),
        ),
        migrations.AlterField(
            model_name="media",
            name="dash_path",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="media",
            name="duration",
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name="media",
            name="format",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="media",
            name="height",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="media",
            name="media_type",
            field=models.CharField(
                choices=[
                    ("IMG", "Image"),
                    ("VID", "Video"),
                    ("AUD", "Audio"),
                    ("<class 'advertisement.models.MediaType.Meta'>", "Meta"),
                ],
                default="IMG",
                max_length=150,
            ),
        ),
        migrations.AlterField(
            model_name="media",
            name="overall_bitrate",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="media",
            name="size",
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name="media",
            name="video_bitrate",
            field=models.CharField(blank=True, default="", max_length=10),
        ),
        migrations.AlterField(
            model_name="media",
            name="width",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
    ]
