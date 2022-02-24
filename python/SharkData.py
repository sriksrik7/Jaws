import datetime
from enum import Enum

class SharkType(Enum):
    SAND_SHARK = 1
    HAMMERHEAD = 2
    DOGFISH = 3

class SharkSighting:
    def __init__(self, id: str, type: SharkType, xCoordinate: float, yCoordinate: float,
                 timestamp: datetime.datetime):
        self.id = id
        self.type = type
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.timestamp = timestamp


    def __repr__(self):
        return "SharkSighting([{0},{1},{2},{3}])".format(self.type, self.xCoordinate, self.yCoordinate, self.timestamp)