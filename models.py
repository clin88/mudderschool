from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from main import mud_app

engine = create_engine(mud_app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

Base = declarative_base()

class Player(Base):
  __tablename__ = 'players'

  id = Column(Integer, primary_key=True)
  public_name = Column(String)
  login = Column(String)
  password = Column(String)
  experience = Column(Integer)

