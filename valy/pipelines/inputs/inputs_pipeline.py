from pathlib import Path

from valy.pipelines.pipeline import Pipeline

from .file_stream import FileStream


class InputPipeline(Pipeline):
    """Pipeline task to capture video stream from file or webcam
    using faster, threaded method to reading video frames."""

    def __init__(self, stream_source: str):
        self.stream = FileStream(Path(stream_source))
        self.stream.start()

        self.frame_num = 0
        super().__init__()

    def generator(self):
        """Yields the frame content and metadata."""

        while True:
            image = self.stream.read()
            if image is None:
                break
            
            self.frame_num += 1
            if self.filter(data):
                yield self.map(data)

    def cleanup(self):
        """Closes video file or capturing device.

        This function should be triggered after the pipeline completes.
        """

        self.stream.stop()