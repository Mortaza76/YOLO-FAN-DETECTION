import os
import shutil

# ✅ Define your exact folder paths
label_dir = "/Users/ameermortaza/Desktop/YOLO Dataset/txt_labels/txt_labels"
folders_to_process = {
    "training": "/Users/ameermortaza/Desktop/YOLO Dataset/old_trainval_images_backup/trainval_images",
    "val": "/Users/ameermortaza/Desktop/YOLO Dataset/val",
    "test_images": "/Users/ameermortaza/Desktop/YOLO Dataset/test_images/test_images"
}

# ✅ Loop through each folder and copy corresponding label files
for folder_name, image_dir in folders_to_process.items():
    print(f"\n📁 Processing folder: {folder_name}")
    
    for filename in os.listdir(image_dir):
        if filename.lower().endswith(".jpg"):
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(label_dir, txt_filename)
            dest_path = os.path.join(image_dir, txt_filename)

            # Copy label if it exists
            if os.path.exists(txt_path):
                shutil.copy(txt_path, dest_path)
                print(f"✅ Copied {txt_filename} to {folder_name}/")
            else:
                print(f"⚠️  Label not found for {filename}")