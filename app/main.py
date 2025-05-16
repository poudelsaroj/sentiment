from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.v1.endpoints import router as sentiment_router
from app.core.config import settings
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Create FastAPI app with metadata
app = FastAPI(
    title=settings.model_name,
    description="Sentiment Analysis API for processing text data",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Middleware to track request processing time"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"Request processed in {process_time:.4f} seconds")
    return response

@app.get("/", tags=["Health"])
def health_check():
    """Health check endpoint to verify service status"""
    return {
        "status": "ok", 
        "env": settings.env,
        "service": "sentiment-analysis",
        "model": settings.model_name
    }

@app.get("/ping", tags=["Health"])
def ping():
    """Simple ping endpoint to check if service is responding"""
    return {"ping": "pong"}

# Exception handler for graceful error responses
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An unexpected error occurred", "error": str(exc)}
    )

# Include the sentiment analysis router
app.include_router(sentiment_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
