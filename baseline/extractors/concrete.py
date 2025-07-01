from pathlib import Path
from base import BaseExtractor

from enums import ExtensionToSave

from av import open, VideoStream, BugError
from av.container import InputContainer

from PIL import Image


class PyAVExtractor(BaseExtractor):
    def extract(self, source: Path, target: Path, extension_to_save: ExtensionToSave = ExtensionToSave.jpg):
        """
        Method, which extracts 1 frame per second from the input video and save to target directory.

        Args:
            source: path to video to parse frames from.
            target: path to folder to save frames to.
            extension_to_save: extension to save an extracted frame to.
        """

        try:
            container: InputContainer = open(file=source)
        except BugError as e:
            raise RuntimeError(f"Cannot open video file {source}: {e}")
        
        if not container.streams.video:
            raise RuntimeError(f"No video stream found in file: {source}")
        
        stream: VideoStream = container.streams.video[0]
        if not stream.average_rate:
            raise RuntimeError(f"Cannot determine FPS for video: {source}")
        
        if not stream.average_rate:
            raise RuntimeError(f"Cannot determine FPS for video: {source}")
        
        fps = float(stream.average_rate)
        if fps <= 0:
            raise RuntimeError(f"Invalid FPS ({fps}) for video: {source}")

        for idx, frame in enumerate(container.decode(stream)):
            if idx % int(fps) == 0:
                try:
                    img: Image.Image = frame.to_image()
                    path: str = f"{target}/{idx}.{extension_to_save.value}"
                    img.save(path)
                except Exception as e:
                    print(f"[WARN] Failed to save frame at idx={idx}: {e}")


