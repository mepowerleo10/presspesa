from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Company, Credit, CreditOffering


@receiver(post_save, sender=CreditOffering)
def generate_credits_on_offering(
    sender, instance: CreditOffering, created: bool, **kwargs
):
    company: Company = instance.to
    amount = instance.amount
    credit = Credit.objects.create(
        initial_value=amount, offered_to=company, current_value=amount
    )
    company.current_credit = credit

    credit.save()
    company.save()
