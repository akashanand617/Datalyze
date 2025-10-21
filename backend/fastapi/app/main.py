from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime
import uvicorn

# Import API routers
from api import health, uploads, pipelines, models, visualizations
from core.config import settings

# Create FastAPI instance
app = FastAPI(
    title="Datalyze API",
    description="Intelligent Data-Pipeline Visualizer & Auto-EDA Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(uploads.router, prefix="/api/v1", tags=["uploads"])
app.include_router(pipelines.router, prefix="/api/v1", tags=["pipelines"])
app.include_router(models.router, prefix="/api/v1", tags=["models"])
app.include_router(visualizations.router, prefix="/api/v1", tags=["visualizations"])

# Root endpoint
@app.get("/", response_model=dict)
async def root():
    """
    Root endpoint for Datalyze API
    
    Returns basic API information and available endpoints.
    """
    return {
        "message": "Welcome to Datalyze API",
        "description": "Intelligent Data-Pipeline Visualizer & Auto-EDA Platform",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/api/v1/health",
        "timestamp": datetime.utcnow().isoformat()
    }

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "message": "An unexpected error occurred",
            "timestamp": datetime.utcnow().isoformat()
        }
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
