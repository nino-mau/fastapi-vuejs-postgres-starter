# FastAPI + Nuxt Starter

A minimal full-stack devlopment starter with FastAPI backend, Nuxt/Bun frontend.

## Quick Start

Create and fill the .env from the .env.example

```bash
cp .env.example .env
```

### Without Docker

```bash
# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
fastapi dev

# Frontend
cd frontend
bun install
bun dev
```

### With Docker

```bash
docker compose up --build -d
```

- API: <http://localhost:8000>
- Frontend: <http://localhost:3000>
