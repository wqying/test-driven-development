# Unit test for Experiment.py
import unittest
from Experiment import Experiment


class TestExperiment(unittest.TestCase):
    def test_init(self):
        exp = Experiment()
        self.assertEqual(exp.condition, [])

    



if __name__ == "__main__":
    unittest.main()
