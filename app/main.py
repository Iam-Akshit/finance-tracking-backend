from fastapi import FastAPI
from . import models
from .database import engine
from .routers import transactions, analytics

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Tracking API",
    description="A backend system for managing and analyzing financial records.",
    version="1.0.0"
)

# Include routers
app.include_router(transactions.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Finance Tracking API. Go to /docs for the interactive API documentation."}