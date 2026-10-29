# Plexivo starter: Python (FastAPI)

A ready-made app for [Plexivo App Runner](https://www.plexivo.io/app-runner/). It listens on port 8080 (or `$PORT`) and answers `/healthz` for health checks.

Edit `main.py`, push to your own repository, and deploy it from Git in the Plexivo console.

Run it locally:

```bash
docker build -t starter .
docker run --rm -p 8080:8080 starter
```
