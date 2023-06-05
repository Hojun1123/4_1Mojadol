from collections import defaultdict
from ultralytics.yolo.engine.connect_db import insertdata, conn
import datetime
from enum import Enum

import cv2
import time
import sys
import os

# 이미 녹화중인지 CHECK
CHECK = 0
class OBJECT(Enum):
    PERSON = 1
    DUMPING = 2
    HOLDED_OBJECT = 3

def main_process(_data, img):
    global CHECK
    global FRAMECOUNT
    #obeject dictionary list
    object_dict = defaultdict(list)
    #0 1 2 : person trash holed_trash
    object_dict[OBJECT.PERSON] = []
    object_dict[OBJECT.DUMPING] = []
    object_dict[OBJECT.HOLDED_OBJECT] = []
    #add objects
    for obj in _data:
        cls_num = int(obj.boxes.cls)
        IMG = img
        if cls_num == 0:
            #OBJECT.PERSON
            print(OBJECT.PERSON)
        elif cls_num == 1:
            #OBJECT.DUMPING
            print(OBJECT.DUMPING)

            if CHECK == 0:
                CHECK = 1
                FRAMECOUNT = 0
                print("record_video")
                nowtime = get_time()
                insertdata(('1234', nowtime))
                fps, w, h = 20, IMG.shape[1], IMG.shape[0]
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                BASE_DIR = 'C:/Users/kkkhh/OneDrive/바탕 화면/경기대4-1/금123_캡스톤_이한용/opotato-master/src/main/resources/static/assets/videos'#os.path.dirname(os.path.abspath(__file__))
                global writer
                writer = cv2.VideoWriter(BASE_DIR + '/' + nowtime + '.mp4', fourcc, fps, (w, h))


        elif cls_num == 2:
            print(OBJECT.HOLDED_OBJECT)
        else:
            ### 발생 x
            print("no_label_error")
            exit(0)

    if CHECK == 1:
        writer.write(img)
        FRAMECOUNT += 1
        if FRAMECOUNT > 100:
            print('end_record')
            writer.release()
            CHECK = 0


    '''
    # trash relationship init
    plist, tlist = [], []
    for obj in obj_list:
        if obj.name == 'person':
            plist.append(obj)
        else:
            tlist.append(obj)
    for i in plist:
        for j in tlist:
            i.check_object_relationship(j)
    print("\n[INFO] Object Relationship")
    for k in [i for i in obj_list if i.name == 'person']:
        print(i, " : ", end=' ')
        for t in k.own_trash:
            print(t,', ', end='')
    '''

def record_video(startTime):
    print("record_video")
    fps, w, h = 30, IMG.shape[1], IMG.shape[0]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    writer = cv2.VideoWriter(BASE_DIR + '/' + get_time() +'.mp4', fourcc, fps, (w, h))

    if not (writer.isOpened()):
        print("File isn't opend!!")
        sys.exit()
    while True:
        writer.write(IMG)  # save video frame
        cv2.waitKey(100)
        nowTime = time.time()
        if startTime + 5 < nowTime:
            print("out")
            break


    print('end_record')
    writer.release()
    global CHECK
    CHECK = 0

def get_time():
    #ex) 230515071311
    return datetime.datetime.now().strftime("%y%m%d%H%M%S")

def print_log_message(_data):
    print('log_message, ', get_time())
    for d in _data:
        print(_data.names[int(d.boxes.cls)], " : ", d.boxes.xywhn)
'''
# person만 own_trash 가짐
class object:
    name = ''
    xywh, xyxy = [], []
    own_trash = []

    def __init__(self, _object):
        cls_num = int(_object.boxes.cls)
        if cls_num == 0:
            self.name = OBJECT.PERSON
        elif cls_num == 1:
            self.name = OBJECT.TRASH
        elif cls_num == 2:
            self.name = OBJECT.HOLDED_PERSON
        else:
            ### 발생 x
            print("no_label_error")
            exit(0)

        self.xywh = list(_object.boxes.xywh)
        self.xyxy = list(_object.boxes.xyxy)

    def __str__(self):
        return str(self.name) + " : " + str(self.xyxy)

    def check_object_relationship(self, _object):
        # self own _object
        # LEFT TOP : 0, 0

        left, top, right, bottom = self.xyxy[0]
        x, y, w, h = _object.xywh[0]

        if left <= x <= right and top <= y <= bottom:
            self.own_trash.append(_object)
            return True
        return False

'''