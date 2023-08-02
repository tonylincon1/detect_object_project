from ultralytics import YOLO

config = '../../config/config.yaml'

model_link = '../train/runs/detect/train2/weights/best.pt'

model = YOLO(model_link)

metrics = model.val(data=config)