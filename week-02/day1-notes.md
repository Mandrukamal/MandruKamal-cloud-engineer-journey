# Concept 1 → IMAGE
            A blueprint/template for a container
            Like a class in programming
            Read-only, reusable

## Docker Image
A lightweight, standalone, and executable software package Includes everything needed to run a piece of software Code, runtime, libraries, and dependencies.

# Concept 2 → CONTAINER
            A running instance of an image
            Like an object created from a class
            Isolated, lightweight

## Docker Container
A running instance of a Docker image. It includes everything needed to run the application, such as the code, runtime, libraries, and dependencies.

# Concept 3 → DOCKERFILE
            A script with instructions to
            BUILD your own custom image
            Every line = one layer

## Dockerfile
A text document that contains all the commands to assemble an image. It is used to automate the process of building Docker images.

# Concept 4 → DOCKER HUB
            Cloud registry for Docker images
            Like GitHub but for containers
            hub.docker.com

## Docker Hub
A cloud-based registry for storing and sharing Docker images. It allows users to upload, download, and manage Docker images in a centralized location.

# Concept 5 → DOCKER DAEMON
            Background service running Docker
            The engine behind everything
            Talks to Docker CLI

## Docker Daemon
The background service that manages Docker containers and images. It is responsible for building, running, and monitoring containers.

# Image vs Container:

Your answer → ✅ CORRECT!
Image     = Template/blueprint (executable software)
Container = Running instance of that image

Perfect analogy to remember:
Image     = A recipe 📄
Container = The actual cooked meal 🍛

# What is FROM in Dockerfile

FROM instruction: Specifies the base image to use for the new image being created. It sets the foundation upon which the rest of the image is built.

FROM does TWO things:
1. ✅ Yes — pulls base image from Docker Hub
2. ➕ More importantly — it sets the FOUNDATION
   of your image. Everything you add in the
   Dockerfile builds ON TOP of this base layer.

Think of it like:
FROM = Choosing your base operating system
       before installing your app on it

# What is -p 8080:8080 in Docker Run command

-p 8080:8080 means PORT MAPPING:

Format → -p HOST_PORT:CONTAINER_PORT

-p 8080:8080 means:
"Map port 8080 on MY laptop
 to port 8080 INSIDE the container"

Real example:
You type    → http://localhost:8080 in browser
Your laptop → forwards that to → container:8080
Container   → runs your Python app on 8080
Browser     → sees your app! 🎉

Nothing to do with Apache — your app was
running Python's built-in HTTP server!

### Quick memory trick for port mapping:

-p HOST:CONTAINER
   YOUR  INSIDE
   MAC   DOCKER