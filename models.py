from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import os

engine = create_engine(os.environ['DATABASE_URL'], echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Player(Base):
  __tablename__ = 'players'

  id = Column(Integer, primary_key=True)
  public_name = Column(String)
  login = Column(String)
  password = Column(String)
  experience = Column(Integer)
  
def validateLogin(login, password):
  session = Session()
  q = session.query(Player).filter(Player.login == login)
  if session.query(q.exists()):
    try:
      user = q.one()
      if user.password == password:
        return {"status":True,"message":"Successful login!", "user":user}
      else:
        return {"status":False,"message":"Incorrect password!"}
    except:
      return {"status":False,"message":"Something's wrong, you might have two identical logins."}
  else:
    return {"status":False,"message":"User does not exist."}
  # What's the interface?
  # Successful login
  # Login exists, wrong password
  # Nothing at all

def createAccount(login, password):
  session = Session()
  q = session.query(Player).filter(Player.login == login)
  if session.query(q.exists()):
    return {"status":False,"message":"Account already exists."}
  else:
    newuser = Player(public_name = login, login = login, password = password, experience = 0)
    session.add(newuser)
    session.commit()
    return {"status":True,"message":"Account created!", "user":newuser}



