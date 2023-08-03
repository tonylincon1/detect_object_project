from ultralytics import YOLO

class Validacao:
    def __init__(self,config,model) -> None:
        self.config = config
        self.model = model

    def validate(self):
        modelo = YOLO(self.model)
        metrics = modelo.val(data=self.config)
        return metrics