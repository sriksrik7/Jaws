import unittest

from backend.attack import SharkAttack


class SharkAttackTest(unittest.TestCase):

    def testSameExactLocation(self):
        latitude = 12
        longitude = 34
        attack = SharkAttack('id', None, latitude, longitude, 'address', 'type', 'activity', 'name', 'MALE', '30',
                             'injury', 'fatal', 'species', 'source', 'link')
        self.assertTrue(attack.isWithinRadius(12, 34, 1))

    def testAboutAMileApart(self):
        latitude = 12.0001
        longitude = 34.004
        attack = SharkAttack('id', None, latitude, longitude, 'address', 'type', 'activity', 'name', 'MALE', '30',
                             'injury', 'fatal', 'species', 'source', 'link')
        self.assertTrue(attack.isWithinRadius(12.02, 34.005, 100))
        self.assertTrue(attack.isWithinRadius(12.02, 34.005, 15))
        self.assertFalse(attack.isWithinRadius(12.02, 34.005, 1))

    def testMiamiBeach(self):
        latitude = 25.597362
        longitude = -79.955848
        attack = SharkAttack('id', None, latitude, longitude, 'address', 'type', 'activity', 'name', 'MALE', '30',
                             'injury', 'fatal', 'species', 'source', 'link')
        self.assertFalse(attack.isWithinRadius(25.736711, -80.201022, 15))
        self.assertTrue(attack.isWithinRadius(25.736711, -80.201022, 20))
        self.assertTrue(attack.isWithinRadius(25.736711, -80.201022, 100))
