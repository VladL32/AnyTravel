# Create the database models

from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base



class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)  # integer primary key will be autoincremented by default
    login = Column(String(255), unique=True, nullable=False)
    user_fname = Column(String(255))
    number = Column(String(255))
    password = Column(String(255), nullable=False)

    # user_cars = db.relationship("Car", back_populates="owner", cascade="all, delete-orphan")

    user_reports = relationship("Reports", back_populates="report_all", cascade="all, delete-orphan")
    user_tours = relationship("Tour",back_populates="tours",cascade="all, delete-orphan")
    def __repr__(self) -> str:
        return f"User(user_id {self.user_id!r}, login={self.login!r},name={self.user_fname!r}, number={self.number!r})"


class Reports(Base):
    __tablename__ = "reports"
    report_id = Column(Integer, primary_key=True)  # integer primary key will be autoincremented by default
    login = Column(String(255), unique=True, nullable=False)
    user_fname = Column(String(255))
    number = Column(String(255))
    reason = Column(String(255))
    report = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    report_all = relationship("User", back_populates="user_reports")

    def __repr__(self) -> str:
        return f"Report(user_id={self.user_id_id!r},login={self.login!r},name={self.user_fname!r}, number={self.number!r}, reason={self.reason!r},report={self.report!r})"


class Tour(Base):
    __tablename__ = "tours"
    tour_id = Column(Integer, primary_key=True)  # integer primary key will be autoincremented by default
    date = Column(String(255))
    people_number = Column(Integer)
    tour_type = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    tours = relationship("User",back_populates="user_tours")
    def __repr__(self) -> str:
        return f"Tour(tour_id {self.tour_id!r}, date={self.date!r},number={self.people_number!r}, number={self.tour_type!r},user_id={self.user_id})"
