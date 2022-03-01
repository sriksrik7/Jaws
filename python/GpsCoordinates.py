import math
from enum import Enum

SQRT_2 = math.sqrt(2)


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
        return -range - coordinate
    elif (coordinate < -range):
        while (coordinate < -range):
            coordinate = coordinate + range
        return range + coordinate
    return coordinate


class GpsCoordinates:
    def __init__(self, x: float, y: float):
        self.x = keepCoordinateInRange(x, 180)
        self.y = keepCoordinateInRange(y, 90)

    def __repr__(self):
        return "GpsCoordinates([{0},{1}])".format(self.x, self.y)


def milesToLongitude(miles: int):
    return miles * 0.0183150183150183


def milesToLatitude(miles: int):
    return miles * 0.0144927536231884


def move(coordinate: GpsCoordinates, miles: int, direction: Direction) -> GpsCoordinates:
    newCoordinate = coordinate
    match direction:
        case Direction.NORTH:
            newCoordinate = GpsCoordinates(coordinate.x, coordinate.y + milesToLongitude(miles))
        case Direction.SOUTH:
            newCoordinate = GpsCoordinates(coordinate.x, coordinate.y - milesToLongitude(miles))
        case Direction.EAST:
            newCoordinate = GpsCoordinates(coordinate.x + milesToLatitude(miles), coordinate.y)
        case Direction.WEST:
            newCoordinate = GpsCoordinates(coordinate.x - milesToLatitude(miles), coordinate.y)
        case Direction.NORTH_EAST:
            newCoordinate = GpsCoordinates(coordinate.x + milesToLatitude(miles // SQRT_2),
                                           coordinate.y + milesToLongitude(miles // SQRT_2))
        case Direction.NORTH_WEST:
            newCoordinate = GpsCoordinates(coordinate.x - milesToLatitude(miles // SQRT_2),
                                           coordinate.y + milesToLongitude(miles // SQRT_2))
        case Direction.SOUTH_EAST:
            newCoordinate = GpsCoordinates(coordinate.x + milesToLatitude(miles // SQRT_2),
                                           coordinate.y - milesToLongitude(miles // SQRT_2))
        case Direction.SOUTH_WEST:
            newCoordinate = GpsCoordinates(coordinate.x - milesToLatitude(miles // SQRT_2),
                                           coordinate.y - milesToLongitude(miles // SQRT_2))
    return newCoordinate


def getCircleOfCoordinates(centerPoint: GpsCoordinates, mileRadius: int) -> [GpsCoordinates]:
    coordinates = []
    for direction in Direction:
        coordinates.append(move(centerPoint, mileRadius, direction))
    return coordinates
