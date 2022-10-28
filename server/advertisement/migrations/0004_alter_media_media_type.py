# Generated by Django 4.1 on 2022-10-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "advertisement",
            "0003_alter_media_audio_bitrate_alter_media_dash_path_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="media",
            name="media_type",
            field=models.CharField(
                choices=[
                    ("IMG", "Image"),
                    ("VID", "Video"),
                    ("AUD", "Audio"),
                    ("<class 'advertisement.models.Media.MediaType.Meta'>", "Meta"),
                ],
                default="IMG",
                max_length=150,
            ),
        ),
    ]
