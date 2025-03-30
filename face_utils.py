import cv2
import dlib

# This code is for Loading the cascade classifier

face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor("models/shape_predictor_68_face_landmarks.dat")


def detect_faces(gray_image, cascade):
    
    faces = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def detect_landmarks(gray_image, face_coordinates):
    
    x, y, w, h = face_coordinates
    dlib_rect = dlib.rectangle(x, y, x + w, y + h)
    landmarks = landmark_predictor(gray_image, dlib_rect)
    return landmarks

def draw_rectangles(image, faces, gray_image):
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        landmarks = detect_landmarks(gray_image, (x, y, w, h))
        if landmarks:
            for i in range(0, 68):
                x_landmark = landmarks.part(i).x
                y_landmark = landmarks.part(i).y
                cv2.circle(image, (x_landmark, y_landmark), 2, (0, 0, 255), -1)

def process_frame(frame, cascade):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detect_faces(gray, cascade)
    draw_rectangles(frame, faces, gray)
    return frame