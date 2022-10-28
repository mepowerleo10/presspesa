from email.policy import default
import uuid
from django.db import models



class Company(models.Model):
    """Model definition for Company."""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=50)
    web_url = models.URLField("Web Page", blank=True, null=True)
    date_joined = models.DateTimeField("Date Joined", auto_created=True, auto_now_add=True)
    is_active = models.BooleanField("Active")
    country = models.CharField(max_length=50, default='Tanzania')
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        """Meta definition for Company."""

        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        """Unicode representation of Company."""
        return self.name


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
        return self.name


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
        return self.name


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
        return f'{self.offered_by}'


