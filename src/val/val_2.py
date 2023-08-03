from ultralytics import YOLO

config = '../../config/config.yaml'
model = '../train/runs/detect/train2/weights/best.pt'

modelo = YOLO(model)
metrics = modelo.val(data=config)

print(metrics.results_dict['metrics/precision(B)'])