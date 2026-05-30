"""FastAPI main application."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path

from backend.database import init_database
from backend.routes import pages, roadmap


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan - startup and shutdown."""
    # Startup
    await init_database()
    print("Database initialized")
    yield
    # Shutdown
    print("Shutting down")


app = FastAPI(
    title="AI Career Roadmap",
    description="Tạo lộ trình học tập cá nhân hóa bằng AI",
    version="1.0.0",
    lifespan=lifespan
)

# Mount static files
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# Include routes
app.include_router(pages.router)
app.include_router(roadmap.router)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "ok",
        "version": "1.0.0",
        "service": "AI Career Roadmap"
    }


@app.get("/sw.js")
async def service_worker():
    """Serve service worker file at root."""
    return FileResponse("sw.js", media_type="application/javascript")
