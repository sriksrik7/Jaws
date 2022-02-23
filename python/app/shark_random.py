import datetime
import random
import uuid
import datetime
import random
from shark_random import randomSighting
from random import randrange

def getSightings(xCoordinate, yCoordinate, maxMiles, fromTime: datetime.datetime, toTime: datetime.datetime) -> [
    SharkSighting]:
    sigthings = []
    for i in range(random.randrange(5,20)):
        sigthings.append(randomSighting(xCoordinate, yCoordinate, maxMiles, fromTime, toTime))
    return sigthings

def randomSighting(xCoordinate: double, yCoordinate: double, maxDistance: double, fromDateTime: datetime.datetime,
                   toDateTime: datetime.datetime) -> SharkSighting:
    sharkId == uuid.UUID.__str__()
    xCoordinate == 1
    yCoordinate == 2
    sharkType == random.choice(list(sharkType))
    timeStamp = datetime.datetime.now()
    return SharkSighting.__init__(sharkId, xCoordinate, yCoordinate, sharkType, timeStamp)
