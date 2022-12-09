import uuid

from django.db import models


class Credit(models.Model):

    initial_value = models.PositiveIntegerField(editable=False)
    current_value = models.PositiveIntegerField(editable=False)
    offered_to = models.ForeignKey("Company", on_delete=models.PROTECT, editable=False)

    class Meta:
        verbose_name = "credit"
        verbose_name_plural = "credits"

    def __str__(self):
        return f"{self.offered_to}"


class CreditOffering(models.Model):
    amount = models.PositiveIntegerField()
    to = models.ForeignKey("Company", on_delete=models.PROTECT)
    on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "credit offering"
        verbose_name_plural = "credit offerings"

    def __str__(self):
        return f"{self.to}"

class CreditDebt(models.Model):
    amount = models.PositiveIntegerField()
    to = models.ForeignKey("Company", on_delete=models.PROTECT)
    on = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "credit debt"
        verbose_name_plural = "credit debts"

    def __str__(self):
        return f"{self.to}"


class Company(models.Model):
    """Model definition for Company."""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=50)
    web_url = models.URLField("Web Page", blank=True, null=True)
    date_joined = models.DateTimeField(
        "Date Joined", auto_created=True, auto_now_add=True
    )
    is_active = models.BooleanField("Active")
    country = models.CharField(max_length=50, default="Tanzania")
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_no = models.CharField(max_length=50, blank=True, null=True)
    current_credit = models.ForeignKey("Credit", blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        """Meta definition for Company."""

        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        """Unicode representation of Company."""
        return f"{self.name} ({self.web_url})"


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
        return f"{self.name} - {self.company}"


class Zone(models.Model):
    """Model definition for Zone."""

    name = models.CharField(max_length=50)
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.SET_NULL,
        help_text="The Compaign that the Zone Belongs to",
        null=True,
        blank=True,
    )

    class Meta:
        """Meta definition for Zone."""

        verbose_name = "Zone"
        verbose_name_plural = "Zones"

    def __str__(self):
        """Unicode representation of Zone."""
        return self.name
