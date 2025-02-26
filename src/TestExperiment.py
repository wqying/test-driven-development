# Unit test for Experiment.py
import unittest
from Experiment import Experiment
from SignalDetection import SignalDetection
import numpy as np


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

    def test_empty_sorted_roc_points(self):
        exp = Experiment()
        with self.assertRaises(ValueError):
            exp.sorted_roc_points()

    def test_sorted_roc_points(self):
        exp = Experiment()
        sdt =  SignalDetection(40, 10, 20, 30)
        sdt2 = SignalDetection(67, 5, 333, 50)
        exp.add_condition(sdt)
        exp.add_condition(sdt2)
        first_element_list = sorted([sdt.false_alarm_rate(), sdt2.false_alarm_rate()])
        second_element_list = [0.8, 0.9305555555555556]
        self.assertEqual(exp.sorted_roc_points(), (first_element_list, second_element_list))

    def test_empty_compute_auc(self):
        exp = Experiment()
        with self.assertRaises(ValueError):
            exp.compute_auc()
    
    def test_compute_auc(self):
        exp = Experiment()
        sdt = SignalDetection(0, 1, 0, 1)  # (0, 0)
        sdt2 = SignalDetection(1, 0, 1, 0)  # (1, 1)
        exp.add_condition(sdt)
        exp.add_condition(sdt2)
        self.assertAlmostEqual(exp.compute_auc(), 0.5, places=2)

    def test_compute_auc_additional(self):
        exp = Experiment()
        sdt = SignalDetection(0, 1, 0, 1)  # (0, 0)
        sdt2 = SignalDetection(1, 0, 1, 0)  # (1, 1)
        sdt3 = SignalDetection(1, 0, 0, 1)  # (0, 1)
        exp.add_condition(sdt)
        exp.add_condition(sdt2)
        exp.add_condition(sdt3)
        self.assertAlmostEqual(exp.compute_auc(), 1, places=2)


if __name__ == "__main__":
    unittest.main()
