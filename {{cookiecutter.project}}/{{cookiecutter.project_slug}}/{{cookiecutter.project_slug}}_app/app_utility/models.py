from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy .orm import relationship
from .database import Base

class Students(Base):
    __tablename__ = 'students'
    sno = Column(Integer, primary_key=True)
    sname = Column(String, nullable=False)
    sclass = Column(String, nullable=True)
    saddr = Column(String,nullable=False)
