# octo-eureka

this repo is for 2024 summer internship projects.

Currently using yolov8 <https://github.com/ultralytics/ultralytics> for detecting human position and skeleton.

## Requirements:
- ### envs:
  - torch 2.3.1+cu118
  - ultralyrics 8.2.57
    '''bash
  pip install ultralytics==8.2.75
    '''
- ### device:
  - webcam(currently using logi C922 PRO 1080P webcam) or cctv

## User Guide:
There are two parts: pose landmarker and cctv tracker.
If using webcam as video stream input, please run calibrate.py for calibrating.
There are four .csv output: camera_distortion, camera_matrix, rotation_vectors and translation_vectors
use camera_distortion and camera_matrix as the input for the calibration function.

- ### Pose Landmarker
  - first, run test.py to train the pre-trained model(either 8l, 8m or 8n. speed: 8n<8m<8l, accuracy:8n<8m<8l)
  - afterwards, change the corresponding directory of best.pt in custom.py
  - then, run custom.py to see the pose landmarking for the video stream

- ### CCTV Tracker
