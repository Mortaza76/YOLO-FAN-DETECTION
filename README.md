# 🧠 YOLO-FAN-DETECTION

This project implements a custom **hand detection system** using the **YOLOv8 object detection framework**. It trains a neural network to detect **hands of a fan** in images and videos.

---

## 📂 Project Structure

```bash
YOLO-FAN-DETECTION/
├── trainval_images/          # Contains training + validation images
├── test_images/              # Contains test images
├── txt_labels/               # Raw label files before sorting
├── dataset.yaml              # Dataset config for YOLOv8
├── train.py                  # Code for training the YOLOv8 model
├── validate_and_test.py      # Code for testing images and measuring performance
├── fan_yolo_model.pt         # Trained model (if not tracked via Git LFS)
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore list
└── README.md                 # This documentation


🧠 Objective

The goal is to detect hands of fans in a custom dataset using YOLOv8, a state-of-the-art object detection architecture. The project covers:
	•	Dataset preparation and labeling.
	•	YOLOv8 training from scratch on custom data.
	•	Image testing and inference.
	•	Model evaluation and metrics (accuracy, precision, recall, mAP).

📦 Dataset Structure

You should organize your dataset into the following directory layout:
trainval_images/
├── img1.jpg
├── img2.jpg
├── ...
├── img1.txt   # YOLO label file
├── img2.txt

test_images/
├── test1.jpg
├── test2.jpg
├── ...
├── test1.txt  # (Optional) for evaluation


🔖 YOLO dataset.yaml

This file tells YOLO where your data and class names are:
path: .  # Root path to dataset
train: trainval_images
val: trainval_images  # or a separate val folder
test: test_images

names:
  0: FAN

🧪 Training the Model

Your training script train.py uses the Ultralytics YOLOv8 API:
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Using YOLOv8 nano as base
model.train(data="dataset.yaml", epochs=50, imgsz=640, batch=16, name="fan_yolo_model2")

Run it with:
python main.py

The trained model will be saved to the runs/detect/fan_yolo_model2/weights/best.pt file.

🧪 Testing & Validation

To run inference on a test image and evaluate model performance:
from ultralytics import YOLO

model = YOLO("runs/detect/fan_yolo_model2/weights/best.pt")

# Run detection on a single image
results = model("test_images/test1.jpg", show=True, save=True)

# Evaluate model performance on test set
metrics = model.val(data="dataset.yaml")
print(metrics)

This will print metrics like:
	•	mAP@0.5
	•	Precision / Recall
	•	Box loss / cls loss


🖼️ How to Test Custom Images
	1.	Place your image in a folder, e.g., test_images/test1.jpg
	2.	Run:

results = model("test_images/test1.jpg", show=True, save=True)
	3.	The output image with bounding boxes will be saved in the runs/detect/predict/ folder.

❗ Common Issues
Issue
Solution
YOLO model not detecting anything
Ensure label .txt files match image filenames and are in YOLO format
GitHub won’t allow push
Remove large files (>100MB) and use .gitignore or Git LFS
Dataset not found
Check paths in dataset.yaml are correct
Model outputs wrong boxes
You may need more training epochs or better data balance


🚀 Future Improvements
	•	Use YOLOv8m or YOLOv8l for better accuracy.
	•	Implement live video stream detection using OpenCV.
	•	Integrate Streamlit/Gradio frontend for real-time testing.

👨‍💻 Author

Ameer Mortaza
Ghulam Ishaq Khan Institute 
Website: Mortaza76.github.io


📜 License

This project is open-sourced for educational and research purposes only. Please contact the author before using for commercial purposes.




















