# Main FastAPI app

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
from fastapi.middleware.wsgi import WSGIMiddleware
from finalproject.app import app

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# craete fastapi (app) instance
fapp = FastAPI()

# need to have an independent database session/connection
# this function lets us to use the same connection throughout request lifecycle
# to accomplish the task above we will use this function as dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    # even if we catch an error the connection is gonna be closed
    finally:
        db.close()

# Depends here is needed to share database connections
@fapp.post("/users/create/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.get_user_by_login(db, user_login=user.login)

    if new_user:
        raise HTTPException(status_code=400, detail="Login is already taken by another user. Use another, dattebayo.")
    return crud.create_user(db=db, user=user)

@fapp.post("/tour/create/", response_model=schemas.Tour)
def create_tour(user_id:int,tour: schemas.TourCreate, db: Session = Depends(get_db)):
    return crud.create_tour(user_id=user_id,db=db, tour=tour)

# # creating a new car
# @fapp.post("/files/", response_model=schemas.File)
# def create_file(user_id:int, car: schemas.FileCreate, db: Session=Depends(get_db)):
#     return crud.create_file(user_id=user_id, db=db, car=car)
@fapp.get("/users/", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    return users

@fapp.get("/tours/", response_model=list[schemas.Tour])
def get_tours(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tour = crud.get_all_tours(db)
    return tour

@fapp.get("/users/fname/{user_fname}", response_model=list[schemas.User])
def get_users_by_name(user_fname, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_user_by_fname(db=db, user_fname=user_fname)
    return users
@fapp.get("/users/{login}", response_model=schemas.User)
def get_certain_user(login, db: Session = Depends(get_db)):
    return crud.get_user_by_login(db, login)

@fapp.get("/tour/{tour_id}",response_model=schemas.Tour)
def get_tour_by_tour_id(tour_id:int,db:Session=Depends(get_db)):
    return crud.get_tour_by_tour_id(db, tour_id)

@fapp.put('/update/tour')
def update_tour(updated_tour:schemas.TourCreate,tour_id:int,db:Session=Depends(get_db)):
    return crud.update_tour_tour_id(db=db,updated_tour=updated_tour,tour_id=tour_id)

@fapp.delete("/delete/{tour_id}")
def delete_tour_by_tour_id(tour_id:int,db: Session = Depends(get_db)):
    return crud.delete_tour_by_tour_id(db=db, tour_id=tour_id)

#
# # getting all cars from db
# @fapp.get("/files/", response_model=list[schemas.File])
# def get_all_files(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return crud.get_all_files(db)
#
# # getting a specific user's cars
# @fapp.get("/user/files/{file_id}", response_model=list[schemas.File])
# def get_user_files(user_id, db: Session = Depends(get_db)):
#     return crud.get_user_files(db, user_id)
#
# # getting a certain car by its id
# @fapp.get("/file/{file_id}/", response_model=schemas.File)
# def get_file(file_id:int, db: Session = Depends(get_db)):
#     return crud.get_file_by_id(db, file_id)
#
#
fapp.mount('/', WSGIMiddleware(app))