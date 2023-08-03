import pytest
from ultralytics import YOLO

def test_yolo_train():
    model_link = 'src/train/runs/detect/train2/weights/best.pt'
    config_yaml = "config/config.yaml"
    model = YOLO(model_link)
    try:
        metrics = model.val(data=config_yaml)
        #assert len(metrics) == 5
    except Exception as e:
        pytest.fail(f"Training failed with exception: {e}")