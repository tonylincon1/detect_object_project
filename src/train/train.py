from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

config_yaml = "../../config/config.yaml"

results = model.train(data=config_yaml, epochs=5)