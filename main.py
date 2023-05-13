import cv2 as cv
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


def annotate_still_image(image_path):
    with mp_pose.Pose(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            min_detection_confidence=0.5) as pose:
        image = cv.imread(image_path)
        image_height, image_width, _ = image.shape
        # Convert the BGR image to RGB before processing.
        results = pose.process(cv.cvtColor(image, cv.COLOR_BGR2RGB))

        print(
            f'Nose coordinates: ('
            f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
            f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
        )

        annotated_image = image.copy()

        mp_drawing.draw_landmarks(
            annotated_image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        cv.imwrite('annotated_image.jpg', annotated_image)


# Webcam for debugging
def annotate_webcam():
    # For webcam input:
    cap = cv.VideoCapture(0)
    with mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            results = pose.process(image)

            # Draw the pose annotation on the image.
            image.flags.writeable = True
            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
            # Flip the image horizontally for a selfie-view display.
            cv.imshow('MediaPipe Pose', cv.flip(image, 1))
            if cv.waitKey(33) == 32:
                break
    cap.release()


def main():
    image_path = 'media/samp.jpg'
    # annotate_still_image(image_path)
    annotate_webcam()


if __name__ == '__main__':
    main()

