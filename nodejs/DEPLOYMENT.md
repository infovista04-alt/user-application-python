# Deployment Guide - user_application_20260213_093948 (Node.js)

## Deployment Options

### 1. Vercel (Recommended for Node.js)
```bash
npm i -g vercel
vercel
```

### 2. Railway
```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

### 3. Render
1. Connect GitHub repo
2. Build: `npm install`
3. Start: `npm start`

### 4. Docker
```bash
docker build -t user_application_20260213_093948-nodejs .
docker run -p 3000:3000 user_application_20260213_093948-nodejs
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| PORT | Server port | 3000 |
| NODE_ENV | Environment | development |
