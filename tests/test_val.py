import pytest

import sys
sys.path.insert(0, "/app") #C:/Users/anton/Desktop/detect_object_project

from src.val.val import Validacao

def test_val():
    config = 'config/config.yaml'
    model = 'src/train/runs/detect/train2/weights/best.pt'
    metrics = Validacao(config,model).validate()
    assert metrics.results_dict['metrics/precision(B)'] > 0.6