from typing import Tuple, Optional
from dataclasses import dataclass


@dataclass
class ColorParams:
    red: float
    green: float
    blue: float
    alpha: float

    @property
    def get_rgb(self) -> Tuple[float, float, float]:
        return self.red, self.green, self.blue


@dataclass
class MetaDisplay:
    num_rects: int = 0
    num_labels: int = 0
    num_lines: int = 0

    rect_params: Optional[str] = None
    text_params: Optional[str] = None
    line_params: Optional[str] = None

    num_arrows: int = 0
    num_circles: int = 0

    arrow_params: Optional[str] = None
    circle_params: Optional[str] = None
