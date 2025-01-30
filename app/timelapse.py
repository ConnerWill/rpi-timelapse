import cv2
import time
import os
from datetime import datetime

IMAGE_DIR = "static"
CAPTURE_INTERVAL = 600  # Capture every 10 minutes

os.makedirs(IMAGE_DIR, exist_ok=True)

def capture_image():
    cam = cv2.VideoCapture(0)  # Use the Pi Camera
    if not cam.isOpened():
        print("Error: Could not open camera.")
        return

    ret, frame = cam.read()
    cam.release()

    if ret:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = os.path.join(IMAGE_DIR, f"{timestamp}.jpg")
        latest_file = os.path.join(IMAGE_DIR, "latest.jpg")

        cv2.imwrite(filename, frame)
        cv2.imwrite(latest_file, frame)  # Overwrite latest frame

        print(f"Captured: {filename}")
    else:
        print("Error: Failed to capture image.")

if __name__ == "__main__":
    while True:
        capture_image()
        time.sleep(CAPTURE_INTERVAL)

