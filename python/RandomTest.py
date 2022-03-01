import unittest
from datetime import datetime

from GpsCoordinates import GpsCoordinates
from Random import getSightings


class SharkRandomTest(unittest.TestCase):

    def testJanuarySharksNearNyc(self):
        fromTime = datetime(2022, 1, 1)
        toTime = datetime(2022, 1, 30)
        mileRadius = 100
        populationSize = 10
        nycCoordinates = GpsCoordinates(40.730610, -73.935242)
        sightings = getSightings(nycCoordinates, mileRadius, populationSize, fromTime, toTime)
        for s in sightings:
            print(repr(s))
        print('Sighting Count: ' + str(len(sightings)))
        self.assertTrue(len(sightings) > 1)
