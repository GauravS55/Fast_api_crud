from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine("sqlite:///krishna.db")
Base = declarative_base()