import unittest
import os
from backend.attack_repo import SharkAttackRepo

os.path.abspath(os.getcwd())

class SharkAttackRepoTest(unittest.TestCase):

    def testAddAllCsv(self):
        repo = SharkAttackRepo(':memory:')
        repo.add(os.path.abspath("backend/test/attacks-test.csv"))
        results = repo.getAll()
        for result in results:
            print(str(result))
