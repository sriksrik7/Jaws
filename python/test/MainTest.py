import unittest

from test.GpsCoordinatesTest import GpsCoordinatesTest
from test.RandomTest import SharkRandomTest

# Main Class to test all unit test classes


class TestAll(unittest.TestCase):

    GpsCoordinatesTest()
    SharkRandomTest()


if __name__ == "__main__":

    unittest.main()
