from flask import Flask, render_template, send_from_directory
import os
import subprocess

app = Flask(__name__)

STATIC_DIR = "static"
VIDEO_FILE = os.path.join(STATIC_DIR, "timelapse.mp4")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/latest.jpg")
def latest_image():
    return send_from_directory(STATIC_DIR, "latest.jpg")

@app.route("/timelapse.mp4")
def timelapse_video():
    return send_from_directory(STATIC_DIR, "timelapse.mp4")

@app.route("/generate-timelapse")
def generate_timelapse():
    images = sorted([f for f in os.listdir(STATIC_DIR) if f.endswith(".jpg")])
    if not images:
        return "No images found", 404

    image_pattern = os.path.join(STATIC_DIR, "%06d.jpg")
    for i, img in enumerate(images):
        os.rename(os.path.join(STATIC_DIR, img), os.path.join(STATIC_DIR, f"{i:06d}.jpg"))

    cmd = [
        "ffmpeg",
        "-r", "10",  # Frames per second
        "-i", image_pattern,
        "-vcodec", "libx264",
        "-pix_fmt", "yuv420p",
        "-y", VIDEO_FILE
    ]

    subprocess.run(cmd, check=True)
    return "Timelapse generated"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

