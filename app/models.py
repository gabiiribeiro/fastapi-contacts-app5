from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# NÃO ESQUECER DE IMPORTAR O BASE DO database.py E APAGAR POIS SENAO VAI DAR CONFLITO
from database import Base

# Base = declarative_base() -- JA ESTA DECLARADA NO MODEL.PY

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    contacts = relationship("Contact", back_populates="owner")

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String)
    email = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="contacts")

