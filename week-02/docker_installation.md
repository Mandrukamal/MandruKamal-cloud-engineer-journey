# Installing Docker Desktop on Mac

## Step 1 — Check your Mac chip first:

Apple Menu () → About This Mac →
Look for either:
→ Apple M1/M2/M3  (Apple Silicon)
→ Intel Core i5/i7 (Intel)

## Step 2 — Download correct version:

Go to: https://www.docker.com/products/docker-desktop/

Click:
→ "Download for Mac - Apple Silicon" if M1/M2/M3
→ "Download for Mac - Intel"        if Intel chip

## Step 3 — Install:

1. Open the downloaded .dmg file
2. Drag Docker to Applications folder
3. Open Docker from Applications
4. Accept the terms
5. Wait for Docker to fully start
   (Watch for whale 🐳 icon in menu bar)
6. Whale icon = Docker is running ✅

## Step 4 — Verify in terminal:

# Check version
docker --version

# Run test container
docker run hello-world
```

---

**You should see this after hello-world:**
```
Hello from Docker! 🎉
This message shows that your installation
appears to be working correctly.
```

---

**⚠️ Common Mac Issues & Fixes:**
```
Issue 1 → Docker slow to start
Fix     → Wait 2-3 mins after opening app
          Watch menu bar whale icon stops
          animating = fully ready

Issue 2 → "Cannot connect to Docker daemon"
Fix     → Make sure Docker Desktop app is
          OPEN and running first

Issue 3 → M1/M2 compatibility warning
Fix     → Make sure you downloaded the
          Apple Silicon version