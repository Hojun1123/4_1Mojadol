from ultralytics import YOLO
from ultralytics.yolo.engine.connect_db import dbconnect
import torch

def main():
    YOLO_MODEL_PATH = r"./best.pt"
    #YOLO_MODEL_PATH "yolov8x.pt"
    model = YOLO(YOLO_MODEL_PATH)

    #webcam source="0", show:추론결과
    print('-------------------------------------------------------------------------------------------------------------')

    ###
    #cuda(gpu) 작동 체크
    #pip install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio===0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
    print(torch.cuda.is_available())

    if dbconnect():
        print("DB Connect")
    else:
        print("Can't connect DB")
        return

    results = model.predict(source="0", show=True, save=True)
    #print(results)

if __name__ == '__main__':
    main()