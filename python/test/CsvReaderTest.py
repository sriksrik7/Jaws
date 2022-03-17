import unittest

import CsvReader


class CsvReaderTest(unittest.TestCase):

    def testCsvReader(self):
        attacks = CsvReader.getSharkAttacks('../attacks1.csv')
        #self.assertTrue(0 < len(attacks))
        for attack in attacks:
            print(attack)
        print('Valid Shark Attacks: ' + str(len(attacks)))
