# # CReateUpdateDelete utils (CRUD)
# # reusable functions to interact with the data in the database.
#
from sqlalchemy.orm import Session
import models, schemas


# getting a user by login from a query to Users table using SQLAlchemy model User
def get_user_by_login(db: Session, user_login: int) -> Session.query:
    return db.query(models.User).filter(models.User.login == user_login).first()

def get_user_by_fname(db: Session, user_fname: str) -> Session.query:
    return db.query(models.User).filter(models.User.user_fname == user_fname).all()

def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> Session.query:
    return db.query(models.User).offset(skip).limit(limit).all()

def get_all_tours(db: Session, skip: int = 0, limit: int = 100) -> Session.query:
    return db.query(models.Tour).offset(skip).limit(limit).all()

def get_tour_by_tour_id(db: Session, tour_id: int) -> Session.query:
    return db.query(models.Tour).filter(models.Tour.tour_id == tour_id).first()

def update_tour_tour_id(db:Session,tour_id:int,updated_tour: schemas.TourCreate):
    tour = get_tour_by_tour_id(db=db,tour_id=tour_id)
    tour.date = updated_tour.date
    tour.tour_type = updated_tour.tour_type
    tour.people_number = updated_tour.people_number
    db.commit()
    db.refresh(tour)
    return tour

def delete_tour_by_tour_id(db: Session, tour_id: int):
    db.query(models.Tour).filter(models.Tour.tour_id == tour_id).delete()
    db.commit()
    return 'Deleted'

def create_tour(db: Session, tour: schemas.TourCreate, user_id) -> models.Tour:
    # new_car = models.Car(car_vendor=car.car_vendor,
    #                         car_model=car.car_model,
    #                         car_owner=user_id)

    new_tour = models.Tour(**tour.dict(), user_id=user_id)
    db.add(new_tour)
    db.commit()
    db.refresh(new_tour)
    return new_tour

#
# # getting a user cars
# def get_user_files(db: Session, user_id: int) -> Session.query:
#     return db.query(models.File).filter(models.File.user_id == user_id).all()
#
#
# # getting all cars
# def get_all_files(db: Session, skip: int = 0, limit: int = 100) -> Session.query:
#     return db.query(models.File).offset(skip).limit(limit).all()
#
#
# # creating a user from instance of UserCreate
def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    new_user = models.User(login=user.login,
                           user_fname=user.user_fname,
                           number=user.number,
                           password=user.password)
    # new_user = models.User(**user.dict()) # this is actually the same as above
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
#
#
# # creating a car from instance of CarCreate
# def create_file(db: Session, file: schemas.FileCreate, user_id) -> models.File:
#     # new_car = models.Car(car_vendor=car.car_vendor,
#     #                         car_model=car.car_model,
#     #                         car_owner=user_id)
#
#     new_file = models.File(**file.dict(), user_id=user_id)
#     db.add(new_file)
#     db.commit()
#     db.refresh(new_file)
#     return new_file
#
#
#
