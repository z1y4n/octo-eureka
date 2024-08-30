import pyrealsense2 as rs # type: ignore
import numpy as np # type: ignore
import cv2 # type: ignore

pipeline_1 = rs.pipeline()
pipeline_2 = rs.pipeline()

config_1 = rs.config()
config_2 = rs.config()

config_1.enable_device('213522250580')
config_2.enable_device('146222251947')

config_1.enable_stream(rs.stream.depth, 840, 480, rs.format.z16, 30) # only depth cam
config_2.enable_stream(rs.stream.depth, 840, 480, rs.format.z16, 30)

pipeline_1.start(config_1)
pipeline_2.start(config_2)

try:
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        frames_1 = pipeline_1.wait_for_frames()
        frames_2 = pipeline_2.wait_for_frames()

        depth_frame_1 = frames_1.get_depth_frame()
        depth_frame_2 = frames_2.get_depth_frame()

        if not depth_frame_1 or not depth_frame_2:
            continue

        depth_image_1 = np.asanyarray(depth_frame_1.get_data())
        depth_image_2 = np.asanyarray(depth_frame_2.get_data())

        depth_colormap_1 = cv2.applyColorMap(cv2.convertScaleAbs(depth_image_1, alpha=0.03), cv2.COLORMAP_JET)
        depth_colormap_2 = cv2.applyColorMap(cv2.convertScaleAbs(depth_image_2, alpha=0.03), cv2.COLORMAP_JET)

        images = np.hstack((depth_colormap_1, depth_colormap_2))
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
finally:
    pipeline_1.stop()
    pipeline_2.stop()
    cv2.destroyAllWindows()