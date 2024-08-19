from ultralytics import YOLO

# Load a model
model = YOLO("yolov8\yolov8s.pt")  # load an official model
# Export the model
model.export(format="engine")
