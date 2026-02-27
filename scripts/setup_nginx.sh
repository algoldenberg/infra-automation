#!/bin/bash

LOG_FILE="logs/provisioning.log"

log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - INFO - $1" | tee -a "$LOG_FILE"
}

# === Production version (Linux server) ===

if command -v nginx &> /dev/null; then
    log "Nginx is already installed, skipping installation."
else
    log "Nginx not found. Installing..."
    apt-get update -y
    apt-get install -y nginx
    log "Nginx installed successfully."
fi
log "Starting Nginx service..."
systemctl start nginx
systemctl enable nginx
log "Nginx service started and enabled."

# === Mock version (Windows/Git Bash simulation) ===
# Uncomment the block below if running from IDE on windows

# log "Checking if Nginx is already installed..."
# log "Nginx not found. Installing..."
# log "Nginx installed successfully."
# log "Starting Nginx service..."
# log "Nginx service started and enabled."