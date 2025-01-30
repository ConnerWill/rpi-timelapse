FROM python:3.11-slim

# Install dependencies
RUN apt-get update

RUN apt-get install -y \
      libopencv-dev \
      ffmpeg \
      v4l-utils \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /app

# Copy project files
COPY app/ /app/
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the web server port
EXPOSE 8000

# Run the timelapse and web server
CMD ["python", "server.py"]
