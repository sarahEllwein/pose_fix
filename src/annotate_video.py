import cv2 as cv
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


def annotate_video(input_video_path):
    with mp_pose.Pose(
            static_image_mode=False,
            model_complexity=2,
            enable_segmentation=True,
            min_detection_confidence=0.5) as pose:

        video = cv.VideoCapture(input_video_path)
        fps = video.get(cv.CAP_PROP_FPS)
        frame_width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

        # Define the codec and create VideoWriter object
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        out = cv.VideoWriter('', fourcc, fps, (frame_width, frame_height))

        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break

            image_height, image_width, _ = frame.shape
            # Convert the BGR frame to RGB before processing.
            results = pose.process(cv.cvtColor(frame, cv.COLOR_BGR2RGB))

            annotated_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            mp_drawing.draw_landmarks(
                annotated_frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
            )

            annotated_frame = cv.cvtColor(annotated_frame, cv.COLOR_RGB2BGR)

            # Write the annotated frame to the output video
            out.write(annotated_frame)

        # Release the video capture and writer objects
        video.release()
        out.release()

    return out
