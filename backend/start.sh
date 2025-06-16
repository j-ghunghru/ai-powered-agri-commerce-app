# Description: Script to activate the virtual environment, install dependencies, and start the FastAPI server.
# Usage: Run this script from the backend directory to set up and start the FastAPI server.
# File: backend/start.sh
# Format: Bash script

#!/bin/bash

echo "Activating virtual environment..."
source venv/Scripts/activate  # For Windows Git Bash
# source venv/bin/activate    # For macOS/Linux

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting FastAPI server..."
uvicorn app.main:app --reload