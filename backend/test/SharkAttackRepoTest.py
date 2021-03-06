import os
import unittest

from backend.attack_repo import SharkAttackRepo

os.path.abspath(os.getcwd())


class SharkAttackRepoTest(unittest.TestCase):

    def testAddAllCsv(self):
        repo = SharkAttackRepo(':memory:')
        repo.addAllCsv(os.path.abspath("backend/test/attacks-test.csv"))
        results = repo.getAll()
        self.assertGreater(len(results), 0)
        for result in results:
            print(str(result))

        australianAttack = repo.getByAddress('Victoria, Australia')
        self.assertEqual('Victoria, Australia', australianAttack[0].address)
