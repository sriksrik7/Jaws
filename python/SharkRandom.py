import datetime
import random
import uuid
import datetime
import random
from random import randrange
from Jaws.python.SharkData import SharkSighting
from Jaws.python.SharkData import SharkType

def getSightings(xCoordinate, yCoordinate, maxMiles, fromTime: datetime.datetime, toTime: datetime.datetime) -> [SharkSighting]:
    sigthings = []
    for i in range(random.randrange(5,20)):
        s = randomSighting(xCoordinate, yCoordinate, maxMiles, fromTime, toTime)
        sigthings.append(s)
    return sigthings

def randomSighting(xCoordinate: float, yCoordinate: float, maxDistance: float, fromDateTime: datetime,
                   toDateTime: datetime) -> SharkSighting:
    xCoordinate = 1
    yCoordinate = 2
    sharkType = random.choice(list(SharkType))
    return SharkSighting( uuid.uuid1(),   sharkType,  xCoordinate, yCoordinate, datetime.datetime.now())
