import datetime
from enum import Enum



class SharkType(Enum):
    SAND_SHARK = 1
    HAMMERHEAD = 2
    DOGFISH = 3

class SharkSighting:
    def __init__(self, id: str, type: SharkType, coordinates: GpsCoordinates, timestamp: datetime.datetime):
        self.id = id
        self.type = type
        self.coordinates = coordinates
        self.timestamp = timestamp

    def __repr__(self):
        return "SharkSighting([{0},{1},{2},{3}])".format(self.type, self.coordinates.x, self.coordinates.y,
                                                         self.timestamp)
