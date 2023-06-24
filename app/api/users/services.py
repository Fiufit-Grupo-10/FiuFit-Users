from attr import dataclass
import math

EARTH_RADIUS = 6371


@dataclass
class Latitude:
    latitude: float


@dataclass
class Longitude:
    longitude: float


class Location:
    latitude: Latitude
    longitude: Longitude

    def __init__(self, latitude: Latitude, longitude: Longitude):
        self.latitude = latitude
        self.longitude = longitude


def distance(origin: Location, target: Location):
    dlat = deg2rad(origin.latitude.latitude - target.latitude.latitude)
    dlong = deg2rad(origin.longitude.longitude - target.longitude.longitude)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(
        deg2rad(origin.latitude.latitude)
    ) * math.cos(deg2rad(target.latitude.latitude)) * math.sin(dlong / 2) * math.sin(
        dlong / 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return EARTH_RADIUS * c


def deg2rad(deg: float):
    return deg * (math.pi / 180)


# function getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2) {
#   var R = 6371; // Radius of the earth in km
#   var dLat = deg2rad(lat2-lat1);  // deg2rad below
#   var dLon = deg2rad(lon2-lon1);
#   var a =
#     Math.sin(dLat/2) * Math.sin(dLat/2) +
#     Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
#     Math.sin(dLon/2) * Math.sin(dLon/2)
#     ;
#   var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
#   var d = R * c; // Distance in km
#   return d;
# }

# function deg2rad(deg) {
#   return deg * (Math.PI/180)
# }
