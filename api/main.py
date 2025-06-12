from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, database
from .database import engine, get_db
from .ai_engine.match import match_produce

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/produce")
def publish_produce(produce: schemas.Produce, db: Session = Depends(get_db)):
    db_produce = models.Produce(**produce.dict())
    db.add(db_produce)
    db.commit()
    db.refresh(db_produce)
    return db_produce

@app.post("/match")
def get_matches(input_data: schemas.MatchInput, db: Session = Depends(get_db)):
    return match_produce(input_data, db)