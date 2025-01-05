#!/bin/bash
set -e

# Read configuration from environment variables
TV_IP=${TV_IP:-"192.168.1.33"}

# Export variables to be accessible by Python script
export TV_IP
export TOKEN_FILE="/config/samsung_token.txt"

# Run the Python script and log output
python /app/brightness_script.py | tee "/config/the_frame_addon.log"
