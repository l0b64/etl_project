from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text


class Fuel_prices(Base):
    __tablename__ = "fuels_dataset"
    id = Column("id", Integer, primary_key=True)
    address = Column("address", Text, nullable=True, unique=False)
    reg_name = Column("reg_name", Text, nullable=True, unique=False)
    brand = Column("brand", Text, nullable=True, unique=False)
    price_e10 = Column("price_e10", Text, nullable=True, unique=False)
    price_sp98 = Column("price_sp98", Text, nullable=True, unique=False)
    price_gazole = Column("price_gazole", Text, nullable=True, unique=False)
    fuel = Column("fuel", Text, nullable=True, unique=False)
    price_e85 = Column("price_e85", Text, nullable=True, unique=False)
    price_gplc = Column("price_gplc", Text, nullable=True, unique=False)
    price_sp95 = Column("price_sp95", Text, nullable=True, unique=False)

    def __repr__(self):
        return f"<Gas station adress={self.adress} brand name={self.brand}>"
