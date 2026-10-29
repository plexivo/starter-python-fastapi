from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Plexivo starter")


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return (
        '<!doctype html><meta charset="utf-8"><title>Hello from Plexivo</title>'
        "<h1>Hello from Plexivo App Runner</h1>"
        "<p>This is the Python (FastAPI) starter. Edit <code>main.py</code>, "
        'or open the <a href="/docs">API docs</a>.</p>'
    )


@app.get("/api/hello")
def hello(name: str = "world") -> dict:
    return {"message": f"Hello, {name}!"}


# Plexivo App Runner sends traffic only once this answers.
@app.get("/healthz")
def healthz() -> dict:
    return {"ok": True}
