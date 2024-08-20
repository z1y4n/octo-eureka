from ultralytics import YOLO

# Load a model
model = YOLO("yolov8\yolov8s-pose.pt")  # load yolov8s.pt
# Export the model
model.export(format="onnx", int8=True) # export to yolov8s.onnx
