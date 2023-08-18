from sqlalchemy import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Auth_User(Base):
    __tablename__ = "auth_user"
    matricula = Column(String, primary_key=True)
    nombre = Column(String(150))
    password = Column(String(128))
