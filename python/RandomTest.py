import unittest
from datetime import datetime

from Jaws.python.GpsCoordinates import GpsCoordinates
from Jaws.python.Random import getSightings


class SharkRandomTest(unittest.TestCase):

    def testGetSharks(self):
        now = datetime.now()
        sightings = getSightings(GpsCoordinates(1, 1), 100, 100, now, now)
        for s in sightings:
            print(repr(s))
        self.assertTrue(len(sightings) > 1)
