# First Dockerfile

Building real container images with Dockerfile.

## Step 1 — Create project folder:

### Navigate to your cloned repo
cd MandruKamal-cloud-engineer-journey

### Create week3 folder structure
mkdir -p week3/lab04-docker
cd week3/lab04-docker

## Step 2 — Create a simple Python app:

### Create app file
touch app.py

Open app.py in VS Code and add:

from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        message = b"Hello from Kamal's Docker Container! 🐳"
        self.wfile.write(message)

if __name__ == "__main__":
    print("Server starting on port 8080...")
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    server.serve_forever()

# Step 3 — Create your Dockerfile:

touch Dockerfile

Open Dockerfile in VS Code and add:

# Base image — official Python on Alpine Linux
FROM python:3.11-alpine

# Set working directory inside container
WORKDIR /app

# Copy our app into the container
COPY app.py .

# Tell Docker this container uses port 8080
EXPOSE 8080

# Command to run when container starts
CMD ["python", "app.py"]

# Step 4 — Build your image:

docker build -t kamal-webapp:v1 .
```

You should see layers being built:
```
Step 1/5 : FROM python:3.11-alpine
Step 2/5 : WORKDIR /app
Step 3/5 : COPY app.py .
Step 4/5 : EXPOSE 8080
Step 5/5 : CMD ["python", "app.py"]
Successfully built xxxxxxxxx
Successfully tagged kamal-webapp:v1 ✅

# Step 5 — Run your container:

docker run -d -p 8080:8080 --name kamal-container kamal-webapp:v1

# Step 6 — Verify it's running:

docker ps

# Step 7 — Test it in browser:

Open browser → http://localhost:8080
You should see → "Hello from Kamal's Docker Container! 🐳"

# Step 8 — Explore your running container:

# See logs
docker logs kamal-container

# Go INSIDE the container
docker exec -it kamal-container sh

# Inside container — look around!
ls
pwd
cat app.py
exit