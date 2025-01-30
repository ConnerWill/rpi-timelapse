# Raspberry Pi Timelapse Camera

This project sets up a Raspberry Pi-based timelapse camera inside a Docker container. It captures images at intervals, generates a timelapse video, and serves both via a web interface.

## **Features**
- Captures images at a set interval (default: 10 minutes).
- Generates a timelapse video using `ffmpeg`.
- Serves images and videos through a web interface.
- Runs entirely in a Docker container for easy setup and deployment.

## **Prerequisites**
- Raspberry Pi (with a camera module attached).
- Raspberry Pi OS (Debian-based Linux).
- Docker and Docker Compose installed.

## **Installation & Setup**
Run the following command to set up everything automatically:

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/yourusername/timelapse-camera/main/setup.sh)"
```

Alternatively, clone and run manually:

```
git clone https://github.com/yourusername/timelapse-camera.git
cd timelapse-camera
bash setup.sh
```

## **Usage**
Once the setup completes, open the web interface:
[http://localhost:8000](http://localhost:8000)


### **Web Interface Features**
- View the latest captured frame.
- Play the generated timelapse video.
- Manually trigger timelapse video generation.

## **Customizing the Capture Interval**
Modify the `CAPTURE_INTERVAL` variable inside `app/timelapse.py`:

```python
CAPTURE_INTERVAL = 600  # Time in seconds (10 minutes)
```

Restart the container for changes to take effect:

```
docker-compose down
docker-compose up --build -d
```

## **Stopping and Removing the Service**
```
docker-compose down
```

To remove the container and images:

```
docker system prune -af
```

---
