import cv2
from ultralytics import YOLO
import torch
from ultralytics.yolo.engine.connect_db import dbconnect
print(torch.cuda.is_available())
if torch.cuda.is_available():
    print('it works')

if dbconnect():
    print("DB Connect")
else:
    print("Can't connect DB")


# Load the YOLOv8 model
model = YOLO('./best0602.pt')

# Open the video file
video_path = "../video/20230421_142846.mp4"
cap = cv2.VideoCapture(video_path)

# save video
#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#out1 = cv2.VideoWriter('./data/record0.mp4', fourcc, 20.0, frame_size)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model.predict(frame, save=True)
        #out1.write(frame)
        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()