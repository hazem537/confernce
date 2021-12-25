from typing import List
from fastapi import Depends,  HTTPException, APIRouter
from sqlalchemy.orm import Session

from .depen import database,schemas,crud

SessionLocal =database.SessionLocal  

router = APIRouter()
Talk = crud.talk()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/talks/{talk_id}", response_model=schemas.Talk)
def read_talk(talk_id: int, db: Session = Depends(get_db)):
    db_talk = Talk.get_talk(db, talk_id=talk_id)
    if db_talk is None:
        raise HTTPException(status_code=404, detail="Talk not found")
    return db_talk



@router.get("/talks/", response_model=List[schemas.Talk])
def read_talks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    talks = Talk.get_talks(db, skip=skip, limit=limit)
    return talks




@router.get("/talksByName/", response_model=schemas.Talk)
def read_talk_name(talk_name: str = "", db: Session = Depends(get_db)):
    db_talk = Talk.get_talk_by_name(db, name=talk_name)
    if db_talk is None:
        raise HTTPException(status_code=404, detail="Talk not found")
    return db_talk


@router.post("/talks/", response_model=schemas.Talk)
def create_talk(talk: schemas.TalkCreate, db: Session = Depends(get_db)):
    return Talk.create_talk(db=db, talk=talk)



@router.put("/talks/{talk_id}", response_model=schemas.Talk)
def update_talk(talk_id: int, talk: schemas.Talk, db: Session = Depends(get_db)):
    db_talk = Talk.get_talk(db, talk_id=talk_id)
    if db_talk is None:
        raise HTTPException(status_code=404, detail="Talk is not founded")
    return Talk.update_talk(db=db, talk_id=talk_id, talk=talk)



@router.delete("/talks/{talk_id}")
def delete_talk(talk_id: int, db: Session = Depends(get_db)):
    db_talk = Talk.get_talk(db, talk_id=talk_id)
    if db_talk is None:
        raise HTTPException(status_code=404, detail="Talk is not founded")
    return Talk.delete_talk(db=db, talk_id=talk_id)




