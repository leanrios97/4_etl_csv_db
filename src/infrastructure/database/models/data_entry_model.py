from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class DataModel(Base):
    __tablename__ = "data_entry"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Float)