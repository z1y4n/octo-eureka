from collections import defaultdict

import cv2
import numpy as np
from numpy import genfromtxt

from ultralytics import YOLO

model = YOLO("yolov8\yolov8n.pt")

cap = cv2.VideoCapture('rtsp://admin:00000@158.132.102.201:8554/live_06', cv2.CAP_FFMPEG)
track_history = defaultdict(lambda: [])

# mtx = genfromtxt('camera_matrix.csv', delimiter=',')
# dist = genfromtxt('camera_distortion.csv', delimiter=',')
# height, width = 384, 640
# new_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (height, width), 0, (height, width))
# map1, map2 = cv2.initUndistortRectifyMap(mtx, dist, None, new_mtx, (height, width), cv2.CV_16SC2)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue
    # calibrate the camera
    # frame = cv2.undistort(frame, mtx, dist, None, new_mtx)
    #dst = cv2.remap(frame, map1, map2, cv2.INTER_LINEAR)
    if success:
        # classes=0 means tracking only person, vid_stride=2 means processing every 2nd frame for speedup processing
        results = model.track(frame, persist=True, tracker="botsort.yaml", conf=0.4, vid_stride=20, classes=0)
        if (results==None or results[0].boxes.id==None):
            continue
        boxes = results[0].boxes.xywh.cpu()
        track_ids = results[0].boxes.id.int().cpu().tolist()
        annotated_frame = results[0].plot()
        for box, track_id in zip(boxes, track_ids):
            x, y, w, h = box
            track = track_history[track_id]
            track.append((float(x), float(y))) # x and y for centre of the bounding box, x and height for the mid point of the lower bound of the bounding box
            if len(track) > 50:
                track.pop(0)
            points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
            cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=10)
        cv2.imshow("YOLOv8 Tracking", annotated_frame)
        if cv2.waitKey(10) & 0xFF == ord("q"): # press q to quit
            cap.release()
            cv2.destroyAllWindows()
            break
