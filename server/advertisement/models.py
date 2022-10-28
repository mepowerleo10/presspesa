import os
import uuid
from typing import Iterable, Optional

from config import settings
from django.db import models
from ffmpeg_streaming import FFProbe
from management.models import Campaign, Company, Zone


class Media(models.Model):
    """Model definition for Media."""

    class MediaType(models.TextChoices):
        """Model definition for MediaTypes."""

        IMAGE = "IMG"
        VIDEO = "VID"
        AUDIO = "AUD"

        class Meta:
            """Meta definition for MediaTypes."""

            verbose_name = "MediaTypes"
            verbose_name_plural = "MediaTypess"

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    campaigns = models.ManyToManyField(Company, blank=True, null=True)
    media_title = models.CharField(max_length=50)
    media_description = models.TextField(max_length=100)
    media_type = models.CharField(
        choices=MediaType.choices, default=MediaType.IMAGE, max_length=150
    )
    file = models.FileField(
        upload_to="videos", default="settings.MEDIA_ROOT/videos/placeholder.file"
    )

    # DASH processing fields
    is_done_processing = models.BooleanField(default=False)
    dash_path = models.CharField(max_length=200, default="", blank=True)
    duration = models.FloatField(default=0.0, blank=True)
    size = models.FloatField(default=0.0, blank=True)
    format = models.CharField(max_length=50, default="", blank=True)
    overall_bitrate = models.CharField(max_length=200, default="", blank=True)
    width = models.CharField(max_length=50, default="", blank=True)
    height = models.CharField(max_length=50, default="", blank=True)
    video_bitrate = models.CharField(max_length=10, default="", blank=True)
    audio_bitrate = models.CharField(max_length=10, default="", blank=True)

    def update_video_metadata(self) -> None:
        input_path = self.file.path
        output_path = f"{settings.MEDIA_ROOT}processed/{self.uuid}"

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ffprobe = FFProbe(input_path)
        ffprobe.save_as_json(os.path.join(output_path, "probe.json"))

        video_format = ffprobe.format()
        first_video = ffprobe.streams().video()
        first_audio = ffprobe.streams().audio()

        self.format = video_format.get("format_name", "Unknown")
        self.duration = float(video_format.get("duration", 0))
        self.size = round(int(video_format.get("size", 0)) / 1024)
        self.overall_bitrate = round(int(video_format.get("bit_rate", 0)) / 1024)
        self.height = first_video.get("width", "Unknown")
        self.width = first_video.get("height", "Unknown")
        self.video_bitrate = round(int(first_video.get("bit_rate", 0)) / 1024)
        self.audio_bitrate = round(int(first_audio.get("bit_rate", 0)) / 1024)

    class Meta:
        """Meta definition for Media."""

        verbose_name = "Media"
        verbose_name_plural = "Media"

    def __str__(self):
        """Unicode representation of Media."""
        return self.media_title


class Advertisement(models.Model):
    """Model definition for Advertisement."""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_created=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    campaigns = models.ManyToManyField(Campaign)
    zone = models.ManyToManyField(Zone)
    media = models.ManyToManyField(Media, blank=True, null=True)

    class Meta:
        """Meta definition for Advertisement."""

        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def __str__(self):
        """Unicode representation of Advertisement."""
        return self.title
