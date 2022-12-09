import os
import shutil
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from config import settings
from management.models import Company, Credit

from .models import Advertisement, CreditAssignment, Media

from .tasks import generate_dash_from_video_upload


@receiver(post_save, sender=Media)
def postprocess_media(sender, instance: Media, created: bool, **kwargs):
    if created:
        if len(instance.file.path) > 0:
            input_path = instance.file.path
            output_path = f"{settings.MEDIA_ROOT}processed/{instance.uuid}"

            if not os.path.exists(output_path):
                os.makedirs(output_path)

            generate_dash_from_video_upload.delay(input_path, output_path, instance.pk)


@receiver(pre_delete, sender=Media)
def cleanup_processed_media(sender, instance: Media, using, origin, **kwargs):
    output_path = f"{settings.MEDIA_ROOT}processed/{instance.uuid}"
    if os.path.exists(output_path):
        shutil.rmtree(output_path)


@receiver(post_save, sender=CreditAssignment)
def generate_credits_on_offering(
    sender, assignment: CreditAssignment, create: bool, **kwargs
):
    company: Company = assignment.by
    advertisement: Advertisement = assignment.to
    credit: Credit = company.current_credit

    credit_value = credit.current_value
    assigned_amount = assignment.amount

    if assigned_amount <= credit_value:
        credit_value = credit_value - assigned_amount
        credit.current_value = credit_value

        advertisement.assigned_credits = (
            advertisement.assigned_credits + assigned_amount
        )

        advertisement.save()
        credit.save()
