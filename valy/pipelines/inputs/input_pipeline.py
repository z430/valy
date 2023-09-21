from pathlib import Path
from loguru import logger

from valy.pipelines.pipeline import Pipeline
import time

from .file_stream import FileStream
from valy.meta import MetaFrame


class InputPipeline(Pipeline):
    """Pipeline task to capture video stream from file or webcam
    using faster, threaded method to reading video frames."""

    def __init__(self, stream_source: Path):
        self.stream = FileStream(stream_source)
        self.stream.start()
        self.frame_num = 0

        self.metadata = MetaFrame(
            stream_source=stream_source,
            stream_source_height=self.stream.height,
            stream_source_width=self.stream.width,
            stream_source_fps=self.stream.fps,
            frame_num=self.frame_num,
        )

        logger.info(self.__class__.__name__)

        super().__init__()

    def generator(self):
        """Yields the frame content and metadata."""

        while True:
            self.metadata.latency = time.perf_counter()
            image = self.stream.read()
            if image is None:
                break

            self.metadata.frame = image
            self.frame_num += 1
            if self.filter(self.metadata):
                yield self.map(self.metadata)

    def cleanup(self):
        """Closes video file or capturing device.

        This function should be triggered after the pipeline completes.
        """

        self.stream.stop()
