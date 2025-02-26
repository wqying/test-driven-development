# Experiment class


class Experiment:
    def __init__(self):
        '''
        Initializes an empty list to store SDT objects and their corresponding labels
        '''
        self.condition = []

    def add_condition(self, sdt_obj: SignalDetection, label: str = None) -> None:
        '''
        Adds a SignalDetection object and an optional label describing the condition to the experiment
        '''
        self.condition.append((sdt_obj, label))

    