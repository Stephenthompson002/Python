# Use Python 3.9 slim image
FROM python:3.9-slim

# Install required system dependencies (for Tkinter and image handling)
RUN apt-get update && apt-get install -y \
    tk \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the app
CMD ["python", "weather_app.py"]
