from ultralytics import YOLO

# should change the directory to the path where the best.pt is located
model = YOLO(r"C:\Users\student\Downloads\yolov8\runs\pose\train\weights\best.pt")

result = model(source=0, show=True,conf=0.3, save=True)