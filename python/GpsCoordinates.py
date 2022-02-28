MILES_TO_LATITUTDE = 0.0144927536231884
MILES_TO_LONGITUDE = 0.0183150183150183


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


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

        def move(direction: Direction, miles: float) -> GpsCoordinates:
            match direction:
                case Direction.NORTH:
                    return GpsCoordinates(x, y + (miles * MILES_TO_LONGITUDE))
                case Direction.SOUTH:
                    return GpsCoordinates(x, y - (miles * MILES_TO_LONGITUDE))
                case Direction.EAST:
                    return GpsCoordinates(x + (miles * MILES_TO_LATITUTDE), y)
                case Direction.WEST:
                    return GpsCoordinates(x - (miles * MILES_TO_LATITUTDE), y)
