#!/bin/bash

set -e  # Exit on any error

# Define variables
REPO_URL="https://github.com/ConnerWill/rpi-timelapse.git"
PROJECT_DIR="${HOME}/timelapse-camera"

printf "Checking if we have everything...\n\n"

if ! command -v git >/dev/null 2>&1; then
  printf "Updating system and installing dependencies...\n"
  sudo apt -y update
  sudo apt -y install git
fi

if ! command -v docker >/dev/null 2>&1; then
  printf "Installing Docker\n\n"
  curl -sSL https://get.docker.com | sh

  printf "Adding current user to the docker group...\n\n"
  sudo usermod -aG docker "${USER}"

  printf "Enabling Docker to start on boot...\n\n"
  sudo systemctl enable docker --now
fi

if ! command -v docker-compose >/dev/null 2>&1; then
  printf "Installing docker-compose...\n\n"
  sudo apt -y update
  sudo apt -y install docker-compose
fi


if [[ -d "${PROJECT_DIR}" ]]; then
  printf "Repository already exists, pulling latest changes...\n\n"
  cd "${PROJECT_DIR}"
  git pull
else
  printf "Cloning the repository...\n\n"
  git clone "${REPO_URL}" "${PROJECT_DIR}"
  cd "${PROJECT_DIR}"
fi

printf "Building and running the Docker container...\n\n"
docker-compose up --build -d

printf "\n\nSetup complete! The timelapse camera will restart automatically after a reboot.\n\n"
printf "Access the timelapse camera at http://%s:8001/\n\n" "$(hostname -I | awk '{print $1}')"
printf "If you added yourself to the docker group, log out and log back in for changes to take effect.\n\n"
