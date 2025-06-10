from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    login_status: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Person(db.Model):
    __tablename__ = "Person"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=True)
    eye_color: Mapped[str] = mapped_column(nullable=True)
    hair_color: Mapped[str] = mapped_column(nullable=True)
    favorites = relationship("Favorites", backref="person", lazy=True)

class Planet(db.Model):
    __tablename__ = "Planet"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[str] = mapped_column(nullable=True)
    terrain: Mapped[str] = mapped_column(nullable=True)
    climate: Mapped[str] = mapped_column(nullable=True)
    favorites = relationship("Favorites", backref="planet", lazy=True)


class Vehicle(db.Model):
    __tablename__ = "Vehicle"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    crew: Mapped[str] = mapped_column(nullable=False)
    manufacturer: Mapped[str] = mapped_column(nullable=False)
    favorites = relationship("Favorites", backref="vehicle", lazy=True)

class Favorites(db.Model):
    __tablename__ = "Favorites"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=False)
    person_id: Mapped[int] = mapped_column(ForeignKey("Person.id"), nullable=False)
    planet_id: Mapped[int] = mapped_column(ForeignKey("Planet.id"), nullable=False)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("Vehicle.id"), nullable=False)