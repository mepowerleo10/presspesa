import os
import shutil
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from config import settings

from .models import Media

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
