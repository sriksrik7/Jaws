import unittest

from app import Csv
from app.SharkAttackRepo import SharkAttackRepo


class SharkAttackRepoTest(unittest.TestCase):

    def testSharkAttackRepo(self):
        attacks = Csv.getSharkAttacksFromProcessedCsv('../attacks-processed.csv')
        repo = SharkAttackRepo(':memory:')
        for attack in attacks:
            repo.add(attack)
        results = repo.getAll()
        for result in results:
            print(str(result))
