import datetime
from enum import Enum


class SharkSighting:
    def __init__(self, id: str, type: SharkType, xCoordinate: double, yCoordinate: double,
                 timestamp: datetime.datetime):
        self.id = id
        self.type = type
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.timestamp = timestamp


class SharkType(Enum):
    SAND_SHARK = 1
    HAMMERHEAD = 2
    DOGFISH = 3
