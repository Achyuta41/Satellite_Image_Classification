# Labeling Guide for Satellite Image Classification

This guide explains the process used for labeling satellite images using **Label Studio** and exporting them in YOLO format.

---

## 🚀 Step 1: Set Up Label Studio
1. Open **Label Studio** and create a new project.
2. Name your project `Satellite Image Classification` and upload the images.
3. Choose the labeling template:
   - Use **Object Detection (Bounding Box)** to mark objects of interest.

---

## 📝 Step 2: Define Label Configuration
1. Go to the **Labeling Interface** and add bounding box labels.
2. For example:
```xml
<View>
  <Image name="image" value="$image" />
  <RectangleLabels name="label" toName="image">
    <Label value="AgriLand" />
    <Label value="Land" />
     <Label value="forest" />
    <Label value="Water" />  
  </RectangleLabels>
</View>
