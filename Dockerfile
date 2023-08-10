# Use the official Python base image from Docker Hub
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY /solutions/ /app/

# Define the command to run your Python script
# CMD ["python", "1.merge-sorted-array.py"]
CMD ["python", "2.remove-element.py"]

