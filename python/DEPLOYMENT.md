# Deployment Guide - user_application_20260213_093948 (Python)

## Deployment Options

### 1. Docker (Recommended)

```bash
# Build image
docker build -t user_application_20260213_093948-python .

# Run container
docker run -d -p 8000:8000 --name user_application_20260213_093948 user_application_20260213_093948-python

# View logs
docker logs -f user_application_20260213_093948
```

### 2. Railway (Free Tier Available)

1. Install Railway CLI: `npm install -g @railway/cli`
2. Login: `railway login`
3. Initialize: `railway init`
4. Deploy: `railway up`

### 3. Render (Free Tier Available)

1. Create account at render.com
2. New Web Service
3. Connect GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### 4. Heroku

```bash
# Login
heroku login

# Create app
heroku create user_application_20260213_093948-python

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### 5. Google Cloud Run

```bash
# Build and push to GCR
gcloud builds submit --tag gcr.io/PROJECT_ID/user_application_20260213_093948

# Deploy
gcloud run deploy user_application_20260213_093948 \
  --image gcr.io/PROJECT_ID/user_application_20260213_093948 \
  --platform managed \
  --allow-unauthenticated
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| PORT | Server port | 8000 |
| DATABASE_URL | Database connection string | - |
| SECRET_KEY | JWT secret key | - |
| DEBUG | Enable debug mode | false |

## Production Checklist

- [ ] Set SECRET_KEY to a secure random string
- [ ] Configure CORS for your domain
- [ ] Set up database connection
- [ ] Enable HTTPS
- [ ] Configure rate limiting
- [ ] Set up monitoring and logging
- [ ] Configure CI/CD pipeline
