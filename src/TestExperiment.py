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
        sdt2 = SignalDetection(1, 2, 3, 4)
        exp.add_condition(sdt, "Condition A")
        exp.add_condition(sdt2, "Condition B")
        self.assertEqual(exp.condition[0][1], "Condition A")
        self.assertEqual(exp.condition[1][1], "Condition B")

    def test_sorted_roc_points(self):
        exp = Experiment()
        with self.assertRaises(ValueError):
            exp.sorted_roc_points()




if __name__ == "__main__":
    unittest.main()
