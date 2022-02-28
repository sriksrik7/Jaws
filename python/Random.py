import datetime
import random

from Jaws.python.GpsCoordinates import GpsCoordinates
from Jaws.python.SharkData import SharkSighting
from Jaws.python.SharkData import SharkType


def randomGpsCoordinates(baseCoordinate: GpsCoordinate, mileRadius) -> GpsCoordinates:
    return


###https://gis.stackexchange.com/questions/235133/checking-if-a-geocoordinate-point-is-land-or-ocean/235195
def getSightings(gpsCoordinate: GpsCoordinates, mileRadius: float, quantity: int, populationSize: int,
                 fromTime: datetime.datetime,
                 toTime: datetime.datetime) -> [
    SharkSighting]:
    if (fromTime > toTime):
        raise ValueError('fromTime cannot be after toTime')

    # Generate random sharks
    # Store them in a dict where key=id, value=type
    sharkDict = {}
    for i in range(populationSize):
        sharkDict[i] = random.choice(list(SharkType))

    maxSecondsAfterFromTime = float(toTime - fromTime)

    sigthings = []
    for i in range(quantity):
        s = randomSighting(populationSize, gpsCoordinate, mileRadius, fromTime, maxSecondsAfterFromTime)
        sigthings.append(s)
    return sigthings


def randomSighting(sharkDict: dict, populationSize: int, gpsCoordinate: GpsCoordinates, fromDateTime: datetime,
                   maxSecondsAfterFromTime: float) -> SharkSighting:
    id = random.randrange(1, populationSize)
    sharkType = sharkDict[id]
    timestamp = fromDateTime + timedelta(seconds=random.randrange(0, maxSecondsAfterFromTime))
    return SharkSighting(id, sharkType, gpsCoordinate, timestamp)
