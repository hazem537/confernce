from typing import Optional
from pydantic import BaseModel
import datetime

#doctor

class DoctorBase(BaseModel):
    name: str
    file_path: Optional[str] = None
    talk_id: int


class DoctorCreate(DoctorBase):
    pass


class Doctor(DoctorBase):
    id: int

    class Config:
        orm_mode = True

#talk
class TalkBase(BaseModel):
    name: str
    start_time: datetime.date
    session_id: int


class TalkCreate(TalkBase):
    pass


class Talk(TalkBase):
    id: int
    doctors: Optional[list[Doctor]] = None

    class Config:
        orm_mode = True

# session 
class SessionBase(BaseModel):
    name: str
    date: datetime.date
    hall_id:int


class SessionCreate(SessionBase):
    pass


class Session(SessionBase):
    id:int
    talks: Optional[list[Talk]] =None

    class Config:
        orm_mode = True

# hall
class HallBase(BaseModel):
    name: str
    from_date: datetime.date
    to_date: datetime.date
    conferance_id:int
   
class HallCreate(HallBase):
    pass

class Hall(HallBase):
    id: int
    sessions: list[Session] =[]
   
    class Config:
        orm_mode = True


# conferance
class ConfBase(BaseModel):
    name: str



class ConfCreate(ConfBase):
    pass

class Conf(ConfBase):
    halls: Optional[list[Hall]] = None
    class Config:
        orm_mode = True


