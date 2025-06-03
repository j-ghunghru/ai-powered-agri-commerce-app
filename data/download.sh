#!/bin/bash

# This script is for downloading data if not running on Kaggle
# Define the URL and the target directory
DATA_URL="https://example.com/path/to/your/dataset.zip"  # Replace with actual URL
TARGET_DIR="data"

if [ -d "/kaggle/input" ]; then
    echo "No download necessary in Kaggle. Using built-in dataset paths."
else
    echo "You are not in the Kaggle environment. Attempting to download data..."

    # Create target directory if it doesn't exist
    mkdir -p "$TARGET_DIR"

    # Download the file
    echo "Downloading dataset from $DATA_URL..."
    curl -L "$DATA_URL" --output "$TARGET_DIR/dataset.zip"

    # Check if download was successful
    if [ $? -eq 0 ]; then
        echo "Download complete. Extracting..."
        unzip -q "$TARGET_DIR/dataset.zip" -d "$TARGET_DIR"
        echo "Extraction complete. Dataset ready in '$TARGET_DIR'."
    else
        echo "Download failed. Please check the URL or your internet connection."
        exit 1
    fi
fi