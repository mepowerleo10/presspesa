import logging

import ffmpeg_streaming as ffstream
from celery import shared_task
from ffmpeg_streaming import Bitrate, Formats, Representation, Size

from .models import Media


@shared_task
def generate_dash_from_video_upload(input_path, output_path, video_id: int):
    logging.basicConfig(
        filename="processing.log", encoding="utf-8", level=logging.DEBUG
    )

    input_video_path = input_path
    output_video_path = output_path
    video = ffstream.input(input_video_path)
    logging.info(f"Success reading {input_video_path}")

    _144p = Representation(Size(256, 144), Bitrate(95 * 1024, 64 * 1024))
    _240p = Representation(Size(426, 240), Bitrate(150 * 1024, 94 * 1024))
    _360p = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
    _480p = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
    _720p = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))

    dash = video.dash(Formats.vp9())
    logging.info("Generating DASH video with h264 codec")
    dash.representations(_144p, _240p, _360p, _480p, _720p)
    logging.info(f"Generating representations for 144p, 240p, 360p, 480p, and 720p")

    logging.info(f"Trying to write output to {output_video_path}")
    dash.output(f"{output_video_path}/dash.mpd")
    logging.info(f"Success writing to {output_video_path}")

    video = Media.objects.get(pk=video_id)

    video.is_done_processing = True
    video.update_video_metadata(input_path, output_path)
    video.save()

    return f"Done processing video {input_video_path}"
