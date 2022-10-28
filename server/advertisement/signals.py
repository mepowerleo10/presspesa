import os
from django.db.models.signals import post_save
from django.dispatch import receiver

from config import settings

from .models import Media

from .tasks import generate_dash_from_video_upload


@receiver(post_save, sender=Media)
def postprocess_media(sender, instance: Media, created: bool, **kwargs):
    if len(instance.file.path) > 0:
        input_path = instance.file.path
        output_path = f"{settings.MEDIA_ROOT}processed/{instance.uuid}"

        if not os.path.exists(output_path):
          os.makedirs(output_path)

        generate_dash_from_video_upload.delay(input_path, output_path)
