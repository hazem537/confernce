from typing import List
from fastapi import Depends,  HTTPException, APIRouter
from sqlalchemy.orm import Session

from .depen import database,schemas,crud

SessionLocal =database.SessionLocal  

router = APIRouter()

Conf = crud.conf() 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/conferances/{conf_id}", response_model=schemas.Conf)
def read_conf(conf_id: int, db: Session = Depends(get_db)):
    db_conf = Conf.get_hall(db, conf_id=conf_id)
    if db_conf is None:
        raise HTTPException(status_code=404, detail="Confrance not found")
    return db_conf


@router.get("/conferances/", response_model=List[schemas.Conf])
def read_confs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    confs = Conf.get_confs(db, skip=skip, limit=limit)
    return confs


@router.post("/conferances/", response_model=schemas.Conf)
def create_conf(conf: schemas.ConfCreate, db: Session = Depends(get_db)):
    return Conf.create_conf(db=db, conf=conf)



@router.put("/conferances/{conf_id}", response_model=schemas.Conf)
def update_conf(conf_id: int, conf: schemas.Conf, db: Session = Depends(get_db)):
    db_conf = Conf.get_conf(db, conf_id=conf_id)
    if db_conf is None:
        raise HTTPException(status_code=404, detail="Conferance is not founded")
    return Conf.update_conf(db=db, conf_id=conf_id, conf=conf)


@router.delete("/conferances/{conf_id}")
def delete_conf(conf_id: int, db: Session = Depends(get_db)):
    db_conf = Conf.get_conf(db,conf_id=conf_id)
    if db_conf is None:
        raise HTTPException(status_code=404, detail="Conferance is not founded")
    return Conf.delete_conf(db=db, conf_id=conf_id)    











