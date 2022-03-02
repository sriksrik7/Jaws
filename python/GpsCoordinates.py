import math
from enum import Enum


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4
    NORTH_EAST = 5
    NORTH_WEST = 6
    SOUTH_EAST = 7
    SOUTH_WEST = 8


## We must handle the scenario where we cross the equator/north pole while adjusting latitude/longitude
## For example, we adjust a latitude of 181 to -179, or a longitude of -91 to 89
def keepCoordinateInRange(coordinate: float, range: float) -> float:
    if (coordinate > range):
        while (coordinate > range):
            coordinate = coordinate - range
        return -range + coordinate
    elif (coordinate < -range):
        while (coordinate < -range):
            coordinate = coordinate + range
        return range + coordinate
    return coordinate


# Longitude = X axis
# Latitude = Y axis
class GpsCoordinates:
    def __init__(self, latitude: float, longitude: float):
        self.longitude = keepCoordinateInRange(longitude, 180)
        self.latitude = keepCoordinateInRange(latitude, 90)

    def __repr__(self):
        return "{0},{1}".format(self.latitude, self.longitude)


def milesToLongitude(miles: int):
    return miles * 0.0183150183150183


def milesToLatitude(miles: int):
    return miles * 0.0144927536231884


def getCoordinatesInAllCardinalDirections(center: GpsCoordinates, mileDistance: int) -> [GpsCoordinates]:
    latitudeShift = milesToLatitude(mileDistance)
    longitudeShift = milesToLatitude(mileDistance)
    coordinates = []
    coordinates.append(GpsCoordinates(center.latitude + latitudeShift, center.longitude))
    coordinates.append(GpsCoordinates(center.latitude - latitudeShift, center.longitude))
    coordinates.append(GpsCoordinates(center.latitude, center.longitude - longitudeShift))
    coordinates.append(GpsCoordinates(center.latitude, center.longitude + longitudeShift))
    return coordinates


def getCoordinatesInAllInterCardinalDirections(center: GpsCoordinates, mileDistance: int) -> [GpsCoordinates]:
    mileShift = mileDistance // math.sqrt(2)
    latitudeShift = milesToLatitude(mileShift)
    longitudeShift = milesToLongitude(mileShift)
    coordinates = []
    coordinates.append(GpsCoordinates(center.latitude + latitudeShift, center.longitude + longitudeShift))
    coordinates.append(GpsCoordinates(center.latitude - latitudeShift, center.longitude - longitudeShift))
    coordinates.append(GpsCoordinates(center.latitude + latitudeShift, center.longitude - longitudeShift))
    coordinates.append(GpsCoordinates(center.latitude - latitudeShift, center.longitude + longitudeShift))
    return coordinates
