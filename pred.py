import glob
from ultralytics import YOLO 
model= YOLO("best.pt")
image_files = glob.glob("D:\projects_github\Satellite_Image_Classification\data\TEST\*.[j][p][g]")
#print(image_files)
for image in image_files:
   model.predict(source=image,show=True,save=True)
   print("ok")