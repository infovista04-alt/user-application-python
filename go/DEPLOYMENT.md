# Deployment Guide - user_application_20260213_093948 (Go)

## Build Binary

```bash
CGO_ENABLED=0 GOOS=linux go build -o user_application_20260213_093948 .
```

## Deploy Options

### 1. Fly.io
```bash
flyctl launch
flyctl deploy
```

### 2. Google Cloud Run
```bash
gcloud run deploy user_application_20260213_093948 --source .
```

### 3. Docker
```bash
docker build -t user_application_20260213_093948-go .
docker run -p 8080:8080 user_application_20260213_093948-go
```
