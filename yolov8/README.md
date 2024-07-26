# octo-eureka

this repo is for 2024 summer internship projects
in this branch, yolov8 pose landmarker is being demo.

requirements:

- env:
  - python 3.10.14(recommanded)
  - ultralytics 8.2.57
  - torch 2.3.1+cu118

- device:
  - webcam(currently using logi C922 PRO 1080P webcam)

user guide:

- first, run test.py to train the pre-trained model(either 8l, 8m or 8n. speed: 8n<8m<8l, accuracy:8n<8m<8l) 
- afterwards, change the corresponding directory of best.pt in custom.py
- then, run custom.py to see the pose landmarking for the video stream
