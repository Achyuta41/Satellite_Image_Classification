from ultralytics import YOLO
import os
import glob
# Load the model
model = YOLO("best.pt")
# Define paths
test_folder = r"D:\projects_github\Satellite_Image_Classification\data\test"
predict_folder = r"D:\projects_github\Satellite_Image_Classification\predict"
# Ensure the predict folder exists
os.makedirs(predict_folder, exist_ok=True)
# Get all image files in the test folder
image_paths = glob.glob(os.path.join(test_folder, "*"))
# Run predictions on all images in the test folder
for img_path in image_paths:
    model.predict(source=img_path, show=True, save=True, project=predict_folder)
