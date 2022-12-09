import os
import uuid

from click import edit

from django.db import models
from django.core.exceptions import ValidationError
from ffmpeg_streaming import FFProbe


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
    campaigns = models.ManyToManyField("management.Company", blank=True, null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    type = models.CharField(
        choices=MediaType.choices, default=MediaType.IMAGE, max_length=150
    )
    file = models.FileField(
        upload_to="videos", default="settings.MEDIA_ROOT/videos/placeholder.file"
    )
    share_count = models.IntegerField(default=0, editable=False)
    view_count = models.IntegerField(default=0, editable=False)

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

    def update_video_metadata(self, input_path, output_path) -> None:

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
        return self.title


class Advertisement(models.Model):
    """Model definition for Advertisement."""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_created=True)
    company = models.ForeignKey("management.Company", on_delete=models.CASCADE)
    campaigns = models.ManyToManyField("management.Campaign")
    zone = models.ManyToManyField("management.Zone")
    media = models.ManyToManyField("Media", blank=True, null=True)
    assigned_credits = models.PositiveBigIntegerField(
        blank=False, null=False, default=0, editable=False
    )
    per_view_credits = models.PositiveIntegerField(blank=False, null=False, default=0)

    class Meta:
        """Meta definition for Advertisement."""

        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def __str__(self):
        """Unicode representation of Advertisement."""
        return self.title


class Reward(models.Model):
    """Model definition for Reward."""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_created=True)
    is_valid = models.BooleanField(default=True)
    offered_by = models.ForeignKey("management.Company", on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(
        "Advertisement", null=True, blank=True, on_delete=models.SET_NULL
    )
    total = models.PositiveBigIntegerField(default=200)
    per_view_value = models.PositiveSmallIntegerField(default=10)

    class Meta:
        """Meta definition for Reward."""

        verbose_name = "Reward"
        verbose_name_plural = "TReward"

    def __str__(self):
        """Unicode representation of Reward."""
        return f"{self.offered_by}"


class CreditAssignment(models.Model):

    by = models.ForeignKey(
        "management.Company", verbose_name="", on_delete=models.DO_NOTHING
    )
    to = models.ForeignKey(
        "Advertisement", verbose_name="", on_delete=models.DO_NOTHING
    )
    amount = models.PositiveIntegerField()

    def validate(self, data):
        company: Company = self.by
        current_credit = company.current_credit
        assigned_amount = self.amount

        if assigned_amount > current_credit:
            raise ValidationError(
                "%(assigned_amount) is greater than the Company's credit",
                params={"assigned_amount": assigned_amount},
            )

    class Meta:
        verbose_name = "Credit Assignment"
        verbose_name_plural = "Credit Assignments"

    def __str__(self):
        return f"{self.by} - {self.to} of {self.amount} credits"
