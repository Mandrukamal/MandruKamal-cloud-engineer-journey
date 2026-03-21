# Base image — official Python on Alpine Linux
FROM python:3.12-alpine

# Set working directory inside container
WORKDIR /app

# Copy our app into the container
COPY app.py .

# Tell Docker this container uses port 8080
EXPOSE 8080

# Command to run when container starts
CMD ["python", "app.py"]