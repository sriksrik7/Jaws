import unittest

from app import Csv


class CsvReaderTest(unittest.TestCase):

    @unittest.skip("This test includes calls to external APIs")
    def testCsvReader(self):
        # Read and enrich source data
        attacks = Csv.readSharkAttacksFromSourceCsv('../attacks-source.csv')

        # Write results (with latitude/longitude enrichment)
        Csv.writeSharkAttacksToCsv(attacks, '../attacks-processed.csv')

        # Read enrich results
        sharkAttacks = Csv.getSharkAttacksFromProcessedCsv('../attacks-processed.csv')

        # Assert results exist
        self.assetTrue(len(sharkAttacks) > 0)

        # Log results
        for shark in sharkAttacks:
            print(shark)
