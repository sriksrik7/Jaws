import datetime
from enum import Enum

from app.deprecated.GpsCoordinates import GpsCoordinates


class SharkType(Enum):
    SAND = 1
    HAMMERHEAD = 2
    DOGFISH = 3
    GREAT_WHITE = 4
    MACKEREL = 5
    SAW = 6
    GROUND = 7


class SharkSighting:
    def __init__(self, id: str, type: SharkType, coordinates: GpsCoordinates, timestamp: datetime.datetime):
        self.id = id
        self.type = type
        self.coordinates = coordinates
        self.timestamp = timestamp

    def __repr__(self):
        return "{0} - [{1}-{2}] {3}".format(self.timestamp, self.id, self.type.name, str(self.coordinates))
