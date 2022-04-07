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
        self.assertTrue(attack.isWithinRadius(12.02, 34.005, 10))
        self.assertFalse(attack.isWithinRadius(12.02, 34.005, 1))
