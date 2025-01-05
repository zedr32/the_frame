# Use the official Python base image
FROM python:3.11-slim

# Set environment variables
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED=1

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir \
    git+https://github.com/nickwaterton/samsung-tv-ws-api.git \
    Pillow \
    urllib3 \
    aiohttp \
    websockets

# Copy add-on files
COPY brightness_script.py /app/
COPY run.sh /app/

# Make the startup script executable
RUN chmod +x /app/run.sh

# Define the startup command
CMD [ "/app/run.sh" ]
