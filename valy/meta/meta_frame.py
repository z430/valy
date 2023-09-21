from dataclasses import dataclass
from pathlib import Path

import numpy as np
from .meta_display import MetaDisplay


@dataclass
class MetaFrame:
    stream_source: Path
    stream_source_height: int
    stream_source_width: int
    stream_source_fps: int

    frame_num: int  # current frame of source

    frame: np.ndarray = np.empty([])

    display_meta: MetaDisplay = MetaDisplay()

    latency: float = 0
