import datetime
import math
import random
from datetime import timedelta

import names
from GpsCoordinates import GpsCoordinates
from GpsCoordinates import getCoordinatesInAllCardinalDirections
from GpsCoordinates import getCoordinatesInAllInterCardinalDirections
from GpsCoordinates import milesToLatitude
from GpsCoordinates import milesToLongitude
from SharkSighting import SharkSighting
from SharkSighting import SharkType
from global_land_mask import globe


def getSightings(gpsCoordinate: GpsCoordinates, mileRadius: int, populationSize: int,
                 fromTime: datetime.datetime,
                 toTime: datetime.datetime) -> [
    SharkSighting]:
    # Validate time range
    if (fromTime > toTime):
        raise ValueError('fromTime cannot be after toTime')

    # Give each shark in the population 1 chance to appear per day
    maxSecondsAfterFromTime = int((toTime - fromTime).total_seconds())
    days = (maxSecondsAfterFromTime / 86400)
    maxPossibleSharkSightings = int(days * populationSize)

    # Confirm water exists in perimeter
    mileScanRadius = mileRadius
    waterCoordinate = None
    while waterCoordinate is None and mileScanRadius > 0:
        waterCoordinate = findWater(getCoordinatesInAllCardinalDirections(gpsCoordinate, mileScanRadius))
        if waterCoordinate is not None:
            waterCoordinate = findWater(getCoordinatesInAllInterCardinalDirections(gpsCoordinate, mileScanRadius))
        # Increment scan distance down 1 mile at a time
        mileScanRadius = mileScanRadius - 1

    # Throw if water is not found
    if (waterCoordinate is None):
        raise ValueError('Water not found within ' + str(mileRadius) + ' miles of ' + repr(gpsCoordinate))

    # Generate shark population
    # Store them in a dict where key=name, value=type
    sharkDict = {}
    for i in range(populationSize):
        sharkDict[names.get_first_name()] = random.choice(list(SharkType))

    # Each iteration through this loop represents a possible shark sighting
    sigthings = []
    for i in range(maxPossibleSharkSightings):

        # Randomly shift x coordinate
        xMileShift = random.randrange(-mileRadius, mileRadius)

        # Use pythagorean theorem to ensure corresponding y coordinate shift stays within max mile radius
        maxYMileShift = int(abs(math.sqrt(math.pow(mileRadius, 2) - math.pow(xMileShift, 2))))
        if maxYMileShift == 0:
            yMileShift = 0
        else:
            yMileShift = random.randrange(-maxYMileShift, maxYMileShift)

        # Execute latitutde/longitude conversions and shift coordinates accordingly
        randomLatitude = gpsCoordinate.latitude + milesToLatitude(yMileShift)
        randomLongitude = gpsCoordinate.longitude + milesToLongitude(xMileShift)

        # If the randomly selected coordinate is in water, it becomes the location of a shark sighting
        if not globe.is_land(randomLatitude, randomLongitude):
            sighting = buildRandomSighting(GpsCoordinates(randomLatitude, randomLongitude), maxSecondsAfterFromTime,
                                           fromTime, sharkDict)
            sigthings.append(sighting)

    # Ensure we always return at least 1 sighting
    if len(sigthings) == 0:
        return [buildRandomSighting(waterCoordinate, maxSecondsAfterFromTime, fromTime, sharkDict)]

    # Sort by timestamp
    sigthings.sort(key=lambda x: x.timestamp, reverse=True)
    return sigthings


def findWater(coordinates: [GpsCoordinates]) -> GpsCoordinates:
    for c in coordinates:
        if not globe.is_land(c.latitude, c.longitude):
            return c
    return None


def buildRandomSighting(gpsCoordinate: GpsCoordinates, maxSecondsAfterFromTime: int,
                        fromTime: datetime.datetime,
                        sharkDict: dict) -> SharkSighting:
    sharkName = random.choice(list(sharkDict.keys()))
    sharkType = sharkDict[sharkName]
    timestamp = fromTime + timedelta(seconds=random.randint(0, maxSecondsAfterFromTime))
    return SharkSighting(sharkName, sharkType, gpsCoordinate, timestamp)
