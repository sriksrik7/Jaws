import unittest
import os
from app.SharkAttackRepo import SharkAttackRepo

os.path.abspath(os.getcwd())

class SharkAttackRepoTest(unittest.TestCase):

    def testAddAllCsv(self):
        repo = SharkAttackRepo(':memory:')
        repo.addAllCsv(os.path.abspath("attacks-processed.csv"))
        results = repo.getAll()
        for result in results:
            print(str(result))
