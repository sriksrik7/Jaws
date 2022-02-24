import unittest

from datetime import datetime
from Jaws.python.SharkRandom import getSightings
from Jaws.python.SharkData import SharkSighting

class SharkRandomTest(unittest.TestCase):

    def testGetSharks(self):
        now = datetime.now()
        sightings = getSightings(100, 100, 100, now, now)
        for s in sightings:
            print(repr(s) )
        self.assertTrue(len(sightings) > 1)
