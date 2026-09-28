from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class LogBase(BaseModel):
    date: Optional[str] = None
    post_charge_percentage: Optional[float] = None
    post_charge_avg_energy_consumption: Optional[int] = None
    post_charge_range: Optional[float] = None
    post_charge_mode: Optional[str] = None
    post_charge_level: Optional[str] = None
    
    post_drive_mode: Optional[str] = None
    post_drive_level: Optional[str] = None
    post_drive_avg_energy_consumption: Optional[int] = None
    remaining_range: Optional[float] = None
    distance_driven: Optional[float] = None
    remaining_percentage: Optional[float] = None

class LogCreate(LogBase):
    pass

class LogUpdate(LogBase):
    pass

class Log(LogBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
