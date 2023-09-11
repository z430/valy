from typing import Tuple
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