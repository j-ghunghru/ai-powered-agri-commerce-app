# Description: This file is part of the AI-Powered-Agri-Commerce project. It initializes the FastAPI application, sets up the database, and includes routers for user and produce management.
# File: backend/app/main.py

# import necessary libraries
from fastapi import FastAPI
from app.routers import user, produce
from app.db.session import init_db

app = FastAPI(title="AI-Powered-Agri-Commerce API", version="1.0.0")

# Initialize database tables
init_db()

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(produce.router, prefix="/produce", tags=["Produce"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
