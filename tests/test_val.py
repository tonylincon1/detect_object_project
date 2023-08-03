import pytest

import sys
sys.path.insert(0, "C:/Users/anton/Desktop/detect_object_project")

from src.val.val import Validacao

def test_val():
    config = '../../config/config.yaml'
    model = '../train/runs/detect/train2/weights/best.pt'
    metrics = Validacao(config,model).validate
    print(metrics)