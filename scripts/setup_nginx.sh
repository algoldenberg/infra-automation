#!/bin/bash

# === Production version (Linux server) ===

if command -v nginx &> /dev/null; then
    echo "[INFO] Nginx is already installed, skipping installation."
else
    echo "[INFO] Installing Nginx..."
    apt-get update -y
    apt-get install -y nginx
    echo "[INFO] Nginx installed successfully."
fi
systemctl start nginx
systemctl enable nginx

# === Mock version (Windows/Git Bash simulation) ===
# Uncomment the block below if running from IDE on windows

# echo "[INFO] Checking if Nginx is already installed..."
# echo "[INFO] Nginx not found. Installing..."
# echo "[INFO] Nginx installed successfully."
# echo "[INFO] Starting Nginx service..."
# echo "[INFO] Nginx service started and enabled."