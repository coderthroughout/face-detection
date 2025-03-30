# Enhanced Real-Time Face Analysis System (Haar Cascade Version)

This project is an enhanced real-time face analysis system built using Python and OpenCV, utilizing the Haar cascade classifier for face detection. It builds upon a basic face detection implementation by adding features like facial landmark detection and a simple GUI for camera resolution control.

## Features

* **Haar Cascade Face Detection:** Uses the Haar cascade classifier for face detection.
* **Facial Landmark Detection:** Detects and displays facial landmarks on the detected faces.
* **Real-time FPS Display:** Shows the frames per second (FPS) for performance monitoring.
* **Camera Resolution Control:** Allows users to adjust the camera resolution via a simple tkinter-based GUI.
* **Modular Code:** The code is organized into separate modules (`face_analysis.py` and `face_utils.py`) for better readability and maintainability.

## Requirements

* Python 3.x
* OpenCV (`opencv-python`)
* dlib (`dlib`)
* tkinter (usually included with Python)

## Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd FaceAnalysis
    ```

2.  **Install the required libraries:**
    ```bash
    pip install opencv-python dlib
    ```

3.  **Download the `shape_predictor_68_face_landmarks.dat` file:**
    * Download `shape_predictor_68_face_landmarks.dat` from a reliable source (e.g., [dlib-models](https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat)).
    * Place the file in the `models` directory within the project.

4.  **Place `haarcascade_frontalface_default.xml`:**
    * Place `haarcascade_frontalface_default.xml` in the `models` directory. You can download it from the opencv github repo.

## Usage

1.  **Run the `face_analysis.py` script:**
    ```bash
    python face_analysis.py
    ```

2.  **GUI Controls:**
    * A tkinter window will appear with sliders to adjust the camera width and height.
    * Click the "Start Face Detection" button to begin face detection.

3.  **Face Detection:**
    * The camera feed will be displayed with rectangles around detected faces and facial landmarks drawn on the face.
    * The real-time FPS will be shown in the top-left corner of the window.

4.  **Exit:**
    * Press the 'q' key (or 'Q') to exit the application.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).
