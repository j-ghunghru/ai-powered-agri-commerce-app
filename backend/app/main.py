from fastapi import FastAPI
from app.routers.produce import router
from app.routers.auth import router as auth_router
from app.db.session import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="BEKN Agri-Commerce API")

# Routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

from app.routers.produce import router as produce_router
app.include_router(produce_router, prefix="/produce", tags=["Produce"])

from app.routers.me import router as me_router
app.include_router(me_router, tags=["User"])
