import cv2
import time
import face_utils
import tkinter as tk
from tkinter import Scale

# Load the cascade classifier
alg = 'models/haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(alg)


camera_width = 640
camera_height = 480


cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

prev_time = 0

def update_resolution(width, height):
    
    global camera_width, camera_height
    camera_width = width
    camera_height = height
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, camera_width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_height)

def run_face_detection():
    
    global prev_time

    while True:
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        ret, img = cam.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        frame = face_utils.process_frame(img, cascade)

        cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("FaceDetect", frame)

        key = cv2.waitKey(1)
        if key == 81 or key == 113:
            break

    cam.release()
    cv2.destroyAllWindows()
    root.destroy() 


root = tk.Tk()
root.title("Face Analysis Control")


width_slider = Scale(root, from_=320, to=1280, orient=tk.HORIZONTAL, label="Width", command=lambda val: update_resolution(int(val), camera_height))
width_slider.set(camera_width)
width_slider.pack()

height_slider = Scale(root, from_=240, to=720, orient=tk.HORIZONTAL, label="Height", command=lambda val: update_resolution(camera_width, int(val)))
height_slider.set(camera_height)
height_slider.pack()


start_button = tk.Button(root, text="Start Face Detection", command=run_face_detection)
start_button.pack()

root.mainloop()