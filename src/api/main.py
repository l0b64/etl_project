from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from database import SessionLocal
import models

app = FastAPI()


class Gas_station_fuel_prices(BaseModel):
    id: int
    address: Optional[str]
    brand: Optional[str]
    fuel_available: Optional[str]
    price_e10: Optional[float]
    price_sp98: Optional[float]
    price_e85: Optional[float]
    price_gplc: Optional[float]
    price_sp95: Optional[float]

    class Config:
        orm_mode = True


db = SessionLocal()


@app.get("/", response_model=List[Gas_station_fuel_prices], status_code=200)
def get_all_gas_stations_with_fuel_prices():
    gas_stations_with_fuel_prices = db.query(models.Fuel_prices).all()
    return gas_stations_with_fuel_prices
