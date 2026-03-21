# Cleanup after lab:

# Stop container
docker stop kamal-container

# Remove container
docker rm kamal-container

# See all images
docker images

# Remove image
docker rmi kamal-webapp:v1
```

---

**📸 Take screenshots of:**
```
1. docker build output
2. docker ps showing container running
3. Browser showing your message
4. docker exec inside container