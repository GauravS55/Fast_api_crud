from sqlalchemy import Column, Integer, String, Text
from database import Base

class Crop(Base):
    __tablename__ = 'crops'
    id = Column(Integer, primary_key=True)
    crop_name = Column(String(256))
    stages = Column(String(256))
    days = Column(Integer)
    image = Column(Text)
    title = Column(String(256))
    task_to_perform = Column(Text)