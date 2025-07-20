from ultralytics import YOLO
import cv2

# Load your trained model (use 'best.pt' for best results)
model = YOLO('/Users/ameermortaza/Desktop/YOLO Dataset/runs/fan_yolo_model2/weights/best.pt')

# Path to your test image
image_path = '/Users/ameermortaza/Desktop/testimage.jpg'

# Run inference
results = model(image_path, show=True, save=True)

# Optional: Access results programmatically
for result in results:
    print(result.boxes)         # Bounding boxes
    print(result.probs)         # Class probabilities (if available)