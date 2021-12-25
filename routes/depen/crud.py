from sqlalchemy.orm import Session

from . import models,schemas
# doctor

class doctor():

    def get_doctor(self,db: Session, doctor_id: int):
      return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()


    def get_doctor_by_name(self,db: Session, name: str):
      return db.query(models.Doctor).filter(models.Doctor.name == name).first()  


    def get_doctors(self,db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Doctor).offset(skip).limit(limit).all()


    def create_doctor(self,db: Session, doctor: schemas.DoctorCreate):
        db_doctor =models.Doctor ( name=doctor.name, file_path=doctor.file_path, talk_id=doctor.talk_id)
        db.add(db_doctor)
        db.commit()
        db.refresh(db_doctor)
        return db_doctor


    def update_doctor(self,db: Session, doctor_id: int, doctor: schemas.Doctor):
        db_doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
        if db_doctor:
            db_doctor.name = doctor.name
            db_doctor.file_path = doctor.file_path
            db.commit()
            db.refresh(db_doctor)
        return db_doctor


    def delete_doctor(self,db: Session, doctor_id: int):
        db_doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
        if db_doctor:
            db.delete(db_doctor)
            db.commit()
        return None
    
# talk

class talk():
    def get_talk(self,db: Session, talk_id: int):
        return db.query(models.Talk).filter(models.Talk.id == talk_id).first()
    
    
    def get_talk_by_name(self,db: Session, name: str):
        return db.query(models.Talk).filter(models.Talk.name == name).first()


    def get_talks(self,db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Talk).offset(skip).limit(limit).all()

    def create_talk(self,db: Session, talk: schemas.TalkCreate):
        db_talk = models.Talk(name=talk.name, start_time=talk.start_time, session_id=talk.session_id)
        db.add(db_talk)
        db.commit()
        db.refresh(db_talk)
        return db_talk

    def update_talk(self,db: Session, talk_id: int, talk: schemas.Talk):
        db_talk = db.query(models.Talk).filter(models.Talk.id == talk_id).first()
        if db_talk:
            db_talk.name = talk.name
            db_talk.start_time = talk.start_time
            db.commit()
            db.refresh(db_talk)
        return db_talk


    def delete_talk(self,db: Session, talk_id: int):
        db_talk = db.query(models.Talk).filter(models.Talk.id == talk_id).first()
        if db_talk:
            db.delete(db_talk)
            db.commit()
        return None    

#session

class session():

    def get_session(self,db: Session, session_id: int):
        return db.query(models.Session).filter(models.Session.id == session_id).first()

    def get_session_by_name(self,db: Session, name: str):
        return db.query(models.Session).filter(models.Session.name == name).first()    

    def get_sessions(self,db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Session).offset(skip).limit(limit).all()

    def create_session(self,db: Session, session: schemas.SessionCreate):
        db_session = models.Session(name=session.name, date=session.date, hall_id=session.hall_id)
        db.add(db_session)
        db.commit()
        db.refresh(db_session)
        return db_session

    def update_session(self,db: Session, session_id: int, session: schemas.Session):
        db_session = db.query(models.Session).filter(models.Session.id == session_id).first()
        if db_session:
            db_session.name = session.name
            db_session.start_time = session.start_time
            db.commit()
            db.refresh(db_session)
        return db_session  

    def delete_session(self,db: Session, session_id: int):
        db_session = (db.query(models.Session).filter(models.Session.id == session_id).first() )
        if db_session:
            db.delete(db_session)
            db.commit()
        return None         

#hall

class hall():
    
    def get_hall(self,db: Session, hall_id: int):
        return db.query(models.Hall).filter(models.Hall.id == hall_id).first()

    def get_halls(self,db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Hall).offset(skip).limit(limit).all()    

    def create_hall(self,db: Session, hall: schemas.HallCreate):
        db_hall = models.Hall(name=hall.name, from_date=hall.from_date,to_date=hall.to_date,conferance_id=hall.conferance_id)
        db.add(db_hall)
        db.commit()
        db.refresh(db_hall)
        return db_hall

    def update_hall(self,db: Session, hall_id: int, hall: schemas.Hall):
        db_hall = (self,db.query(models.Hall).filter(models.Hall.id == hall_id).first())
        if db_hall:
                db_hall.name = hall.name
                db_hall.from_date = hall.from_date
                db_hall.to_date = hall.to_date
                db_hall.conferance_id = hall.conferance_id
                db.commit()
                db.refresh(db_hall)
        return db_hall

    def delete_hall(self,db: Session, hall_id: int):
        db_hall = ( db.query(models.Hall).filter(models.Hall.id == hall_id).first()   )
        if db_hall:
            db.delete(db_hall)
            db.commit()
        return None


class conf():
    def get_conf(self,db: Session, conf_id: int):
        return db.query(models.Conferance).filter(models.Conferance.id == conf_id).first()

    def get_confs(self,db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Conferance).offset(skip).limit(limit).all()        

    
    def create_conf(self,db: Session, conf: schemas.ConfCreate):
        db_conf = models.Conferance(name=conf.name)
        db.add(db_conf)
        db.commit()
        db.refresh(db_conf)
        return db_conf

    def update_conf(self,db: Session, conf_id: int, conf: schemas.Conf):
        db_conf = (self,db.query(models.Conferance).filter(models.Conferance.id == conf_id).first())
        if db_conf:
                db_conf.name = conf.name
                db.commit()
                db.refresh(db_conf)
        return db_conf

    def delete_conf(self,db: Session, conf_id: int):
        db_conf = ( db.query(models.Conferance).filter(models.Conferance.id == conf_id).first()  )
        if db_conf:
            db.delete(db_conf)
            db.commit()
        return None
    
