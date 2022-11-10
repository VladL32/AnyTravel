# Create the Pydantic models
# To avoid confusion between the SQLAlchemy models and the Pydantic models,
# we will have the file models.py with the SQLAlchemy models, and the file schemas.py
# with the Pydantic models.

# These Pydantic models define more or less a "schema" (a valid data shape).

# pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
# Define how data should be in pure, canonical Python; validate it with pydantic.

from pydantic import BaseModel


# Create an CarBase and UserBase Pydantic models or just schemas
# to have common attributes while creating or reading data.

# class FileBase(BaseModel):
#     file_path: str
#
#
# class FileCreate(FileBase):
#     pass
#
#
# # will be used when reading data, when returning it from the API.
# # Config class: Behaviour of pydantic can be controlled via the Config class on a model or a pydantic dataclass
# # orm_mode: will tell the Pydantic model to read the data even if it is not a dict, but an ORM model
# class File(FileBase):
#     file_id: int
#     user_id: int
#
#     class Config:
#         orm_mode = True

class TourBase(BaseModel):
    date: str
    people_number: int
    tour_type: str

class TourCreate(TourBase):
    pass

class Tour(TourBase):
    tour_id: int
    user_id: int

    class Config:
        orm_mode = True




class UserBase(BaseModel):
    login: str
    user_fname: str
    number: str


class UserCreate(UserBase):
    password: str


# will be used when reading data, when returning it from the API.
class User(UserBase):
    user_id: int
    user_tours: list[Tour] = []

    class Config:
        orm_mode = True
