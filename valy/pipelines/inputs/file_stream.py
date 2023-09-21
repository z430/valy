from pathlib import Path

import numpy as np
import cv2
from imutils.video import FileVideoStream


class FileStream:
    def __init__(self, stream_path: Path) -> None:
        assert stream_path.exists()
        self.stream = FileVideoStream(str(stream_path))
        self.height = int(self.stream.stream.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.width = int(self.stream.stream.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.fps = int(self.stream.stream.get(cv2.CAP_PROP_FPS))

    def start(self) -> None:
        self.stream.start()

    def read(self) -> np.ndarray:
        return self.stream.read()

    def stop(self) -> None:
        self.stream.stop()
