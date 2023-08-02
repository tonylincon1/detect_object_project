from ultralytics import YOLO

model_link = '../train/runs/detect/train2/weights/best.pt'

model = YOLO(model='yolov8x.pt') #,names=({2: 'car',5: 'bus',7: 'truck'})

results = model(['../data/inference/inference_test.png'],save=True,conf=0.4,augment=True,classes=[2,5,7],show=True) #

print(results)