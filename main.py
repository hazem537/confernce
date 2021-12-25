from fastapi import  FastAPI

from routes import doctor,talk,session,hall,conferance

from routes.depen import  models

from routes.depen import database
from routes.depen.crud import conf 
SessionLocal= database.SessionLocal
engine=database.engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(doctor.router)
app.include_router(talk.router)
app.include_router(session.router)
app.include_router(hall.router)
app.include_router(conferance.router)






