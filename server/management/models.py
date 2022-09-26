import uuid
from django.db import models


class Address(models.Model):
    """Model definition for Address."""

    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        """Meta definition for Address."""

        verbose_name = "Address"
        verbose_name_plural = "Addresss"

    def __str__(self):
        """Unicode representation of Address."""
        pass


class Company(models.Model):
    """Model definition for Company."""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=50)
    web_url = models.URLField("Web Page", blank=True, null=True)
    date_joined = models.DateTimeField("Date Joined", auto_created=True)
    is_active = models.BooleanField("Active")
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Company."""

        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        """Unicode representation of Company."""
        pass


class Campaign(models.Model):
    """Model definition for Campaign."""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, help_text="Company Running the Campaign"
    )

    class Meta:
        """Meta definition for Campaign."""

        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"

    def __str__(self):
        """Unicode representation of Campaign."""
        pass


class Zone(models.Model):
    """Model definition for Zone."""

    name = models.CharField(max_length=50)
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        help_text="The Compaign that the Zone Belongs to",
    )

    class Meta:
        """Meta definition for Zone."""

        verbose_name = "Zone"
        verbose_name_plural = "Zones"

    def __str__(self):
        """Unicode representation of Zone."""
        pass


class Token(models.Model):
    """Model definition for Token."""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_created=True)
    is_valid = models.BooleanField(default=True)
    offered_by = models.ForeignKey(Company, on_delete=models.CASCADE)
    count = models.PositiveBigIntegerField(default=200)
    token_value = models.FloatField()

    class Meta:
        """Meta definition for Token."""

        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def __str__(self):
        """Unicode representation of Token."""
        pass


class Advertisement(models.Model):
    """Model definition for Advertisement."""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_created=True)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    campaigns = models.ManyToManyField(Campaign)
    zone = models.ManyToManyField(Zone)

    class Meta:
        """Meta definition for Advertisement."""

        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def __str__(self):
        """Unicode representation of Advertisement."""
        pass


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

        def __str__(self):
            """Unicode representation of MediaTypes."""
            pass

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
        pass
