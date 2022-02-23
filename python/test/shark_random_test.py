import unittest

from datetime import datetime
from python.app.shark_random import randomSighting


class SharkRandomTest(unittest.TestCase):

    def getSharks(self):
        now = datetime.datetime.now()
        sightings = randomSighting(100, 100, 100, now - datetime.timedelta(1, 0), now)
        self.assertTrue(len(sightings) > 1)
