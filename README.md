# octo-eureka

this repo is for 2024 summer internship projects.


## RealSense

### Required Environment:
- python v3.9/v3.10(recommanded)
- Mediapipe v0.10.14
- openCV 4.10.0
- numpy v2.0.0
- matplotlib v3.9.1

### User Guide:
there are three modules in this repo: Face Landmarker, Hand Landmarker and Combined landmarker.

- the Combined landmarker is designed for tracking the driver status(gazing direction, dazing warning, hands status)
- press 'run all' in the script to process the landmarker.
- the outout would show the current status, and give warning sign when target losses or dangerous move is detected
- press 'q' to quit the landmarker.

## YOLO

Currently using yolov8 <https://github.com/ultralytics/ultralytics> for detecting human position and skeleton.

### Requirements:
- ### envs:
  - torch 2.3.1+cu118
  - ultralyrics 8.2.57
    '''bash
  pip install ultralytics==8.2.75
    '''
- #### device:
  - webcam(currently using logi C922 PRO 1080P webcam) or cctv

### User Guide:
There are two parts: pose landmarker and cctv tracker.
If using webcam as video stream input, please run calibrate.py for calibrating.
There are four .csv output: camera_distortion, camera_matrix, rotation_vectors and translation_vectors
use camera_distortion and camera_matrix as the input for the calibration function.

- #### Pose Landmarker
  - first, run test.py to train the pre-trained model(either 8l, 8m or 8n. speed: 8n<8m<8l, accuracy:8n<8m<8l)
  - afterwards, change the corresponding directory of best.pt in custom.py
  - then, run custom.py to see the pose landmarking for the video stream

- #### CCTV Tracker
