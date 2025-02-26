# Unit test for Experiment.py
import unittest
from Experiment import Experiment
from SignalDetection import SignalDetection


class TestExperiment(unittest.TestCase):
    def test_init(self):
        exp = Experiment()
        self.assertEqual(exp.condition, [])

    def test_add_condition(self):
        exp = Experiment()
        sdt =  SignalDetection(40, 10, 20, 30)
        exp.add_condition(sdt, "Condition A")
        self.assertEqual(exp.condition[0][1], "Condition A")



if __name__ == "__main__":
    unittest.main()
