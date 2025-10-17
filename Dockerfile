# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Run the application
CMD ["python", "app.py"]