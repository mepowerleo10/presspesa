from django.db import models
import uuid
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from management.models import Campaign, Zone, Company

# Create your models here.
class Advertisement(models.Model):
    """Model definition for Advertisement."""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_created=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    campaigns = models.ManyToManyField(Campaign)
    zone = models.ManyToManyField(Zone)

    class Meta:
        """Meta definition for Advertisement."""

        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def __str__(self):
        """Unicode representation of Advertisement."""
        return self.title


class Media(models.Model):
    """Model definition for Media."""

    class MediaType(models.TextChoices):
        """Model definition for MediaTypes."""

        IMAGE = 1
        VIDEO = 2
        AUDIO = 3

        class Meta:
            """Meta definition for MediaTypes."""

            verbose_name = "MediaTypes"
            verbose_name_plural = "MediaTypess"

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    media_title = models.CharField(max_length=50)
    media_description = models.TextField(max_length=100)
    media_type = models.SmallIntegerField(choices=MediaType.choices, default=MediaType.IMAGE
    )

    class Meta:
        """Meta definition for Media."""

        verbose_name = "Media"
        verbose_name_plural = "Media"

    def __str__(self):
        """Unicode representation of Media."""
        return self.media_title