from collections import defaultdict

import threading, time
import queue

import cv2
import numpy as np
from numpy import genfromtxt

import ultralytics
from ultralytics import YOLO

model = YOLO("yolov8\yolov8s.onnx", task="detect")  # load an official model
ultralytics.checks()

q=queue.Queue()
cap = cv2.VideoCapture('rtsp://admin:00000@158.132.102.201:8554/live_06',cv2.CAP_FFMPEG)
# lock = threading.Lock()
def Receive():
    ret, frame = cap.read()
    q.put(frame) # put the first frame into the queue
    while ret:
        ret, frame = cap.read()
        q.put(frame)
        # if cap.get(cv2.CAP_PROP_BUFFERSIZE) > 1:
        #     cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)


def Display():
    track_history = defaultdict(lambda: [])
    while True:
        if q.empty() !=True:
            frame=q.get()
            results = model.track(frame, persist=True, tracker="botsort.yaml", conf=0.35, vid_stride=1, classes=0)
            if (results==None or results[0].boxes.id==None):
                continue

            boxes = results[0].boxes.xywh.cpu()
            track_ids = results[0].boxes.id.int().cpu().tolist()
            annotated_frame = results[0].plot()
            for box, track_id in zip(boxes, track_ids):
                x, y, w, h = box
                track = track_history[track_id]
                track.append((float(x), float(y))) # x and y for centre of the bounding box, x and height for the mid point of the lower bound of the bounding box
                if len(track) > 200:
                    track.pop(0)
                points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=10)
            cv2.imshow("YOLOv8 Tracking", annotated_frame) 

        if cv2.waitKey(5) & 0xFF == ord("q"): # press q to quit
            print("Quitting...")
            cap.release()
            cv2.destroyAllWindows()
            break     

p1 = threading.Thread(target=Receive)
p2 = threading.Thread(target=Display)
p1.start()
p2.start()
   