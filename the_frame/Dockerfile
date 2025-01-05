# Use the official Python base image
FROM python:3.11-slim

# Set environment variables
ENV LANG C.UTF-8

# Install necessary packages
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install the Git repository
RUN pip install --no-cache-dir git+https://github.com/nickwaterton/samsung-tv-ws-api.git

# Copy addon files
COPY brightness_script.py /app/
COPY run.sh /app/

# Make the startup script executable
RUN chmod +x /app/run.sh

# Define the startup command
CMD [ "/app/run.sh" ]
