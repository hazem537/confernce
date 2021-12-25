from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


from .import database 
Base = database.Base


class Doctor(Base):
    __tablename__ = "Doctors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    file_path = Column(String)
    talk_id = Column(Integer, ForeignKey("Talks.id"))
    talk = relationship("Talk", cascade="all,delete", back_populates="doctors")


class Talk(Base):
    __tablename__ = "Talks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    start_time = Column(DateTime)
    doctors = relationship("Doctor", cascade="all,delete", back_populates="talk")
    session_id = Column(Integer, ForeignKey("Sessions.id"))
    session = relationship("Session", cascade="all,delete", back_populates="talks")


class Session(Base):
    __tablename__ = "Sessions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date = Column(DateTime)
    talks = relationship("Talk", cascade="all,delete", back_populates="session")
    hall_id = Column(Integer, ForeignKey("halls.id"))
    hall = relationship("Hall", cascade="all,delete", back_populates="sessions")



class Hall(Base):
    __tablename__ = "halls"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    from_date = Column(DateTime)
    to_date = Column(DateTime)
    sessions = relationship("Session", cascade="all,delete", back_populates="hall")
    conferance_id = Column(Integer, ForeignKey("conferances.id"))
    conferance = relationship("Conferance", cascade="all,delete", back_populates="halls")


class Conferance(Base):
    __tablename__ = "conferances"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    halls = relationship("Hall", cascade="all,delete", back_populates="conferance")

