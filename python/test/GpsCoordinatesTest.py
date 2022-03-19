import unittest

from app.deprecated.GpsCoordinates import GpsCoordinates


class GpsCoordinatesTest(unittest.TestCase):

    def testGetters(self):
        latitude = 35.652832
        longitude = 139.839478
        cords = GpsCoordinates(latitude, longitude)
        self.assertEqual(latitude, cords.latitude)
        self.assertEqual(longitude, cords.longitude)

    def testPositiveLimits(self):
        latitude = 100
        longitude = 181
        cords = GpsCoordinates(latitude, longitude)
        self.assertEqual(-80, cords.latitude)
        self.assertEqual(-179, cords.longitude)

    def testNegativeLimits(self):
        latitude = -91
        longitude = -200
        cords = GpsCoordinates(latitude, longitude)
        self.assertEqual(89, cords.latitude)
        self.assertEqual(160, cords.longitude)

