from ultralytics import YOLO

# Load the model.
model = YOLO('../project/yolov8n.pt')

# Training.
results = model.train(
    data='custom_data.yaml',
    imgsz=640,
    epochs=10,
    batch=8,
    name='yolov8n_custom')