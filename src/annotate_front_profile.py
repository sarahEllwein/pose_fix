import cv2 as cv
import numpy as np
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


def check_feet_position(coordinates):
    # Extract coordinates for relevant landmarks
    left_ankle = coordinates[mp_pose.PoseLandmark.LEFT_ANKLE]
    right_ankle = coordinates[mp_pose.PoseLandmark.RIGHT_ANKLE]
    left_hip = coordinates[mp_pose.PoseLandmark.LEFT_HIP]
    right_hip = coordinates[mp_pose.PoseLandmark.RIGHT_HIP]

    feet_outwards_threshold = 0.2
    feet_inwards_threshold = 0.1

    # Calculate the distances between the ankles and hips
    left_distance = abs(left_ankle[0] - left_hip[0])
    right_distance = abs(right_ankle[0] - right_hip[0])

    # Determine feet position
    if left_distance > feet_outwards_threshold or right_distance > feet_outwards_threshold:
        # Feet are too outwards
        return "Too Outwards"
    elif left_distance < feet_inwards_threshold or right_distance < feet_inwards_threshold:
        # Feet are too inwards
        return "Too Inwards"
    else:
        # Feet position is good
        return "Good Position"


def calculate_angle(hip_point, knee_point):
    # Calculate the angle between the lines formed by the hip and knee points
    dx = knee_point[0] - hip_point[0]
    dy = knee_point[1] - hip_point[1]
    return math.degrees(math.atan2(dy, dx))


def check_knee_alignment(coordinates_list):
    result = []

    for coordinates in coordinates_list:
        hip_point_left = coordinates[mp_pose.PoseLandmark.LEFT_HIP]
        knee_point_left = coordinates[mp_pose.PoseLandmark.LEFT_KNEE]

        hip_point_right = coordinates[mp_pose.PoseLandmark.RIGHT_HIP]
        knee_point_right = coordinates[mp_pose.PoseLandmark.RIGHT_KNEE]

        lAngle = calculate_angle(hip_point_left, knee_point_left)
        rAngle = calculate_angle(hip_point_right, knee_point_right)

        if lAngle or rAngle < 10:
            result.append("Good alignment")
        elif lAngle or rAngle < 20:
            result.append("Poor alignment")
        else:
            result.append("Excessive misalignment")

    return result


