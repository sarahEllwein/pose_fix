import os
import shutil
import json

import cv2 as cv
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


def annotate_still_image(image_path):
    image = cv.imread(image_path)
    annotated_image = image.copy()
    with mp_pose.Pose(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            min_detection_confidence=0.5
    ) as pose:
        image_height, image_width, _ = image.shape
        # Convert the BGR image to RGB before processing.
        results = pose.process(cv.cvtColor(image, cv.COLOR_BGR2RGB))

        mp_drawing.draw_landmarks(
            annotated_image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

    return annotated_image


def main():
    test_root = os.path.join(os.getcwd(), 'testset')

    # Create resset directory
    res_root = os.path.join(os.getcwd(), 'resset')

    # Remove directory if exists
    if os.path.exists(res_root):
        shutil.rmtree(res_root)

    os.mkdir(res_root)
    print("Directory '%s' created" % res_root)

    testset = os.listdir(test_root)
    testset.remove('.DS_Store')

    for imagename in testset:
        print('Annotating', imagename)
        image_path = os.path.join(test_root, imagename)
        img = annotate_still_image(image_path)

        cv.imwrite(os.path.join(res_root, imagename), img)

    # annotate_still_image(image_path)
    # annotate_webcam()


if __name__ == '__main__':
    main()
