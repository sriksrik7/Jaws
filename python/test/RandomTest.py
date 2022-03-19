import unittest
from datetime import datetime

from app.deprecated.GpsCoordinates import GpsCoordinates
from app.deprecated.Random import getSightings


class SharkRandomTest(unittest.TestCase):

    def getAndValidateSightings(self, coordinates, mileRadius, populationSize, fromTime, toTime):
        sightings = getSightings(coordinates, mileRadius, populationSize, fromTime, toTime)

        sharkNames = set()
        for sighting in sightings:
            print(sighting)
            self.assertTrue(sighting.timestamp <= toTime)
            self.assertTrue(sighting.timestamp >= fromTime)
            self.assertIsNotNone(sighting.coordinates)
            self.assertIsNotNone(sighting.type)
            sharkNames.add(sighting.id)

        self.assertTrue(len(sightings) > 0)
        self.assertTrue(len(sharkNames) <= populationSize)

    def testOneMonthOfSharksNearNyc(self):
        fromTime = datetime(2022, 1, 1)
        toTime = datetime(2022, 1, 30)
        mileRadius = 100
        populationSize = 10
        nyc = GpsCoordinates(40.730610, -73.935242)
        self.getAndValidateSightings(nyc, mileRadius, populationSize, fromTime, toTime)

    def testOneWeekOfSharksNearKeyWest(self):
        fromTime = datetime(2022, 11, 1)
        toTime = datetime(2022, 11, 7)
        mileRadius = 50
        populationSize = 10
        keyWest = GpsCoordinates(24.555059, -81.779984)
        self.getAndValidateSightings(keyWest, mileRadius, populationSize, fromTime, toTime)

    def testOneDayOfSharksNearOuterBanks(self):
        fromTime = datetime(2022, 11, 6)
        toTime = datetime(2022, 11, 7)
        mileRadius = 20
        populationSize = 1
        outerBanks = GpsCoordinates(39.656635, -74.175465)
        self.getAndValidateSightings(outerBanks, mileRadius, populationSize, fromTime, toTime)

    def testOneYearfSharksNearJapan(self):
        fromTime = datetime(2021, 11, 1)
        toTime = datetime(2022, 11, 7)
        mileRadius = 10
        populationSize = 10
        japan = GpsCoordinates(35.6733766,139.8765446)
        self.getAndValidateSightings(japan, mileRadius, populationSize, fromTime, toTime)
