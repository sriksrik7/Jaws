import unittest

from app import Csv


class CsvReaderTest(unittest.TestCase):

    def testCsvReader(self):
        attacks = Csv.readSharkAttacksFromSourceCsv('../attacks-source.csv')
        Csv.writeSharkAttacksToCsv(attacks, '../attacks-processed.csv')
        sharkAttacks = Csv.getSharkAttacksFromProcessedCsv('../attacks-processed.csv')
        for shark in sharkAttacks:
            print(shark)
