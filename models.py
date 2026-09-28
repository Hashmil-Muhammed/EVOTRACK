from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from sqlalchemy.sql import func
from database import Base

class CarBatteryLog(Base):
    __tablename__ = "car_battery_logs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True, nullable=True) # Storing as YYYY-MM-DD string for simplicity
    
    post_charge_percentage = Column(Float, nullable=True)
    post_charge_avg_energy_consumption = Column(Integer, nullable=True)
    post_charge_range = Column(Float, nullable=True)
    post_charge_mode = Column(String, nullable=True)
    post_charge_level = Column(String, nullable=True)
    
    post_drive_mode = Column(String, nullable=True)
    post_drive_level = Column(String, nullable=True)
    post_drive_avg_energy_consumption = Column(Integer, nullable=True)
    remaining_range = Column(Float, nullable=True)
    distance_driven = Column(Float, nullable=True)
    remaining_percentage = Column(Float, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
