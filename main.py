from ultralytics import YOLO

# Load YOLOv8 model (YOLOv8n is the nano version, fastest; you can change to v8s, v8m, etc.)
model = YOLO('yolov8n.pt')  # or 'yolov8s.pt'

# Train the model
model.train(
    data='/Users/ameermortaza/Desktop/YOLO Dataset/dataset.yaml',
    epochs=50,
    imgsz=640,
    batch=8,
    name='fan_yolo_model',
    project='/Users/ameermortaza/Desktop/YOLO Dataset/runs',
)