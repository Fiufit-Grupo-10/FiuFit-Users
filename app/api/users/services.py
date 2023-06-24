from typing import NewType, Self
from attr import dataclass
import math

EARTH_RADIUS = 6371

Latitude = NewType('Latitude', float)
Longitude = NewType('Longitude', float)
Kilometers = NewType('Kilometers', float)


def deg2rad(deg: float) -> float:
    return deg * (math.pi / 180)


class Location:
    latitude: Latitude
    longitude: Longitude

    def __init__(self, latitude: Latitude, longitude: Longitude):
        self.latitude = latitude
        self.longitude = longitude

    def distance(self, to: Self) -> Kilometers:
        latitude_difference = deg2rad(self.latitude - to.latitude)
        longitude_difference = deg2rad(self.longitude - to.longitude)
        x = math.sin(latitude_difference / 2)
        y = math.sin(longitude_difference / 2)
        a = (x * x) + math.cos(deg2rad(self.latitude)) * math.cos(
            deg2rad(to.latitude)
        ) * (y * y)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return Kilometers(EARTH_RADIUS * c)
