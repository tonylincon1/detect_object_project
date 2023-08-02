from ultralytics import YOLO

model_link = '../train/runs/detect/train2/weights/best.pt'

model = YOLO(model='yolov8x.pt') #model_link

results = model.track(source="https://www.youtube.com/watch?v=_kBLiYS8wms", conf=0.3, iou=0.5, show=True)