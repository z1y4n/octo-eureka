# octo-eureka

this repo is for 2024 summer internship projects.

Currently using yolov8 <https://github.com/ultralytics/ultralytics> for detecting human position and skeleton.

## Requirements:
- ### envs:
  - torch 2.3.1+cu118
  - ultralyrics 8.2.57
- ### device:
  - webcam(currently using logi C922 PRO 1080P webcam) or cctv

## User Guide:

There are two parts: pose landmarker and cctv tracker.

If using webcam as video stream input, please run calibrate.py for calibrating.

There are four .csv output: camera_distortion, camera_matrix, rotation_vectors and translation_vectors

use camera_distortion and camera_matrix as the input for the calibration function.

- ### Pose Landmarker (./yolov8)
  - first, run train.py to train the pre-trained model(either 8l, 8m or 8n. speed: 8n<8m<8l, accuracy:8n<8m<8l)
  - afterwards, change the corresponding directory of best.pt in custom.py
  - then, run custom.py to see the pose landmarking for the video stream

- ### CCTV Tracker (./cctv_tracking)
  - run gpu_test.py for testing if GPU and CUDA are available.
  - in case there is a need for changing into another model/format, use model_convert.py for converting.
  - check if the url of CCTV and the directory of the model are correct.
  - run track.py
