from ultralytics import YOLO 
model= YOLO("best.pt")
model.predict(source="1.jpg",show=True,save=True)
model.predict(source="2.jpg",show=True,save=True)
model.predict(source="3.png",show=True,save=True)
model.predict(source="4.jpg",show=True,save=True)
model.predict(source="5.jpg",show=True,save=True)
model.predict(source="6.jpg",show=True,save=True)
model.predict(source="7.jpg",show=True,save=True)