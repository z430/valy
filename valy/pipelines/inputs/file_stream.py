from pathlib import Path

import numpy as np
from imutils.video import FileVideoStream


class FileStream:
    def __init__(self, stream_path: Path) -> None:
        assert stream_path.exists()
        self.stream = FileVideoStream(str(stream_path))

    def start(self) -> None:
        self.stream.start()

    def read(self) -> np.ndarray:
        return self.stream.read()
    
    def stop(self) -> None:
        self.stream.stop()