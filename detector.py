# detector.py
from ultralytics import YOLO
from PIL import Image

model = YOLO("yolov8n.pt")  # You can use any YOLOv8 model you prefer

def run_detection(image_path):
    results = model(image_path)
    res_plotted = results[0].plot()
    return Image.fromarray(res_plotted)
