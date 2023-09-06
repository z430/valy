from typing import List
from dataclasses import dataclass

@dataclass
class MetaObjects:
    class_id: int
    object_id: int
    confidence: float
    detector_bbox_info: List
    tracker_bbox_info: List
    obj_label: str