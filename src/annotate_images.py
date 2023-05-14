import cv2 as cv
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


def l2_norm(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** (1 / 2)


# take image path and outputs image numpy array object and landmarks
def get_image_info(image_path):
    img = cv.imread(image_path)
    with mp_pose.Pose(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            min_detection_confidence=0.5) as pose:
        # Convert the BGR image to RGB before processing.
        res = pose.process(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    return img, res


def is_side_profile(img, res):
    image_height, image_width, _ = img.shape
    left_shoulder_point = (
        res.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x * image_width,
        res.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * image_height
    )
    right_shoulder_point = (
        res.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * image_width,
        res.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * image_height
    )
    nose_point = (
        res.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width,
        res.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height
    )
    return l2_norm(left_shoulder_point, right_shoulder_point) < l2_norm(left_shoulder_point, nose_point)


def annotate_still_image(img):
    annotated_image = img.copy()
    with mp_pose.Pose(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            min_detection_confidence=0.5
    ) as pose:
        image_height, image_width, _ = img.shape
        # Convert the BGR image to RGB before processing.
        results = pose.process(cv.cvtColor(img, cv.COLOR_BGR2RGB))

        mp_drawing.draw_landmarks(
            annotated_image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

    return annotated_image
