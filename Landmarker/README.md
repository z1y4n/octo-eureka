# octo-eureka

this repo is for 2024 summer internship projects

currently using mediapipe library <https://github.com/google-ai-edge/mediapipe> for basic functions implementation

- Required Environment:
  - python v3.9/v3.10(recommanded)
  - Mediapipe v0.10.14
  - openCV 4.10.0
  - numpy v2.0.0
  - matplotlib v3.9.1

- there are three modules in this repo: Face Landmarker, Hand Landmarker and Combined landmarker.
- the Combined landmarker is designed for tracking the driver status(gazing direction, dazing warning, hands status).

- press 'run all' in the script to process the landmarker.
- the output would show the current status, and give warning sign when target losses or dangerous move is detected.
- press 'q' to quit the landmarker.
