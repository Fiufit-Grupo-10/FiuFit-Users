from typing import NewType
import math
from app.api.users import models, crud
from sqlalchemy.orm import Session

EARTH_RADIUS = 6371

Latitude = NewType("Latitude", float)
Longitude = NewType("Longitude", float)
Kilometers = NewType("Kilometers", float)


def deg2rad(deg: float) -> float:
    return deg * (math.pi / 180)


class Location:
    latitude: Latitude
    longitude: Longitude

    def __init__(self, latitude: Latitude, longitude: Longitude):
        self.latitude = latitude
        self.longitude = longitude

    def distance(self, other) -> Kilometers:
        latitude_difference = deg2rad(self.latitude - other.latitude)
        longitude_difference = deg2rad(self.longitude - other.longitude)
        x = math.sin(latitude_difference / 2)
        y = math.sin(longitude_difference / 2)
        a = (x * x) + math.cos(deg2rad(self.latitude)) * math.cos(
            deg2rad(other.latitude)
        ) * (y * y)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return Kilometers(EARTH_RADIUS * c)


def filter_trainers_by_distance(
    user: models.User, distance: float, db: Session
) -> list[models.User]:
    user_location = Location(latitude=user.latitude, longitude=user.longitude)
    trainers = crud.get_trainers(db=db)
    distant_trainers = []
    for trainer in trainers:
        trainer_location = Location(
            latitude=trainer.latitude, longitude=trainer.longitude
        )
        if user_location.distance(other=trainer_location) <= distance:
            distant_trainers.append(trainer)

    return distant_trainers
