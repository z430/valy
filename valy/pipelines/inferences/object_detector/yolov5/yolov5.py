""" default yolov5 torch model """

import torch
import numpy as np


class YoloV5:
    def __init__(self) -> None:
        self.model = torch.hub.load("ultralytics/yolov5", "yolov5s")

    def forward(self, image: np.ndarray) -> np.ndarray:
        return np.empty([])
