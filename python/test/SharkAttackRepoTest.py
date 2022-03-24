import unittest

from app.SharkAttackRepo import SharkAttackRepo


class SharkAttackRepoTest(unittest.TestCase):

    def testSharkAttackRepo(self):
        repo = SharkAttackRepo(':memory:')
        repo.addAllCsv('../attacks-processed.csv')
        results = repo.getAll()
        for result in results:
            print(str(result))
