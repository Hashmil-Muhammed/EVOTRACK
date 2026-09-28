from sqlalchemy.orm import Session
import models
import schemas
from datetime import datetime

def get_logs(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.CarBatteryLog).order_by(models.CarBatteryLog.date.desc().nulls_last(), models.CarBatteryLog.id.desc()).offset(skip).limit(limit).all()

def get_log(db: Session, log_id: int):
    return db.query(models.CarBatteryLog).filter(models.CarBatteryLog.id == log_id).first()

def create_log(db: Session, log: schemas.LogCreate):
    db_log = models.CarBatteryLog(**log.model_dump())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def update_log(db: Session, log_id: int, log_update: schemas.LogUpdate):
    db_log = get_log(db, log_id)
    if not db_log:
        return None
    
    update_data = log_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_log, key, value)
    
    db.commit()
    db.refresh(db_log)
    return db_log

def delete_log(db: Session, log_id: int):
    db_log = get_log(db, log_id)
    if db_log:
        db.delete(db_log)
        db.commit()
        return True
    return False
