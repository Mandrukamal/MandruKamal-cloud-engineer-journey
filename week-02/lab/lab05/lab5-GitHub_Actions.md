# LAB 05 — GitHub Actions CI/CD Pipeline

What we're building:

You push code to GitHub
        ↓
GitHub Actions triggers automatically
        ↓
Pipeline builds your Docker image
        ↓
Runs tests
        ↓
Shows green checkmark ✅
        ↓
That's CI/CD in action!


# Step 1 — Create workflow folder structure:

## Make sure you're in your repo root
cd MandruKamal-cloud-engineer-journey

## Create GitHub Actions folder
mkdir -p .github/workflows

## Create your pipeline file
touch .github/workflows/ci.yml

# Step 2 — Write your CI pipeline:

Open .github/workflows/ci.yml in VS Code and add exactly this:

name: Cloud Engineer CI Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Build Docker image
        run: |
          docker build -t kamal-webapp:${{ github.sha }} ./week3/lab04-docker

      - name: Verify Docker image exists
        run: |
          docker images kamal-webapp

      - name: Run container test
        run: |
          docker run -d -p 8080:8080 --name test-container kamal-webapp:${{ github.sha }}
          sleep 3
          curl http://localhost:8080
          docker stop test-container
          docker rm test-container

      - name: Pipeline success message
        run: |
          echo "✅ CI Pipeline completed successfully!"
          echo "🐳 Docker image built and tested!"
          echo "🚀 Built by: Kamal Kumar Mandru"

# Step 3 — Commit and push:

git add .
git commit -m "ci: add GitHub Actions CI pipeline for Docker build"
git push origin main
```

---

### Step 4 — Watch it run! 🎬
```
Go to → github.com/Mandrukamal/
         MandruKamal-cloud-engineer-journey
Click → Actions tab
Watch → Your pipeline running in real time!
```

---

### Step 5 — What to look for:
```
🟡 Yellow circle  = Pipeline running
✅ Green check    = Pipeline passed!
❌ Red cross      = Something failed
                    (come back to me with
                    the error message)
```

---

**📸 Screenshots to take:**
```
1. Your ci.yml file in VS Code
2. GitHub Actions tab showing pipeline running
3. Green checkmark — pipeline passed! ✅
4. Click into the pipeline — show each step