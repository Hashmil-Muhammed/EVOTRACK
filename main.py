from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse
import traceback
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
import crud
from database import engine, get_db
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Car Battery Log API")

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return PlainTextResponse(f"Global Exception: {traceback.format_exc()}", status_code=500)


# Mount static files
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Setup templates
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/api/logs", response_model=List[schemas.Log])
def read_logs(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    return crud.get_logs(db, skip=skip, limit=limit)

@app.post("/api/logs", response_model=schemas.Log)
def create_log(log: schemas.LogCreate, db: Session = Depends(get_db)):
    return crud.create_log(db, log)

@app.patch("/api/logs/{log_id}", response_model=schemas.Log)
def update_log(log_id: int, log: schemas.LogUpdate, db: Session = Depends(get_db)):
    db_log = crud.update_log(db, log_id=log_id, log_update=log)
    if db_log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return db_log

@app.delete("/api/logs/{log_id}")
def delete_log(log_id: int, db: Session = Depends(get_db)):
    success = crud.delete_log(db, log_id=log_id)
    if not success:
        raise HTTPException(status_code=404, detail="Log not found")
    return {"message": "Log deleted successfully"}
