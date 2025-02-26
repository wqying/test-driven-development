# Experiment class
from SignalDetection import SignalDetection

class Experiment:
    def __init__(self):
        '''
        Initializes an empty list to store SDT objects and their corresponding labels
        '''
        empty_list = []
        self.condition = empty_list

    def add_condition(self, sdt_obj: SignalDetection, label: str = None) -> None:
        '''
        Adds a SignalDetection object and an optional label describing the condition to the experiment
        '''
        self.condition.append((sdt_obj, label))  # made this into a tuple so that the object and label is connected

    def sorted_roc_points(self) -> tuple[list[float], list[float]]:
        '''
        Return sorted false alarm rates and hit rates for plotting the ROC curve
        '''
        pass
         