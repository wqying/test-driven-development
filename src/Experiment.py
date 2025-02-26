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

    def sorted_roc_points(self) -> tuple[list[float], list[float]]:  # This method was created with the help of ChatGPT
        '''
        Return sorted false alarm rates and hit rates for plotting the ROC curve
        '''
        # If no conditions are present, raise ValueError
        if len(self.condition) == 0:
            raise ValueError
        
        false_alarm_rates = []
        # Since self.condition is a list, we can iterate through the elements inside
        # Note that the elements inside self.condition are tuples, so we need to iterate through both of them
        for sdt_obj, _ in self.condition:  # we ignore the labels, so we use '_'
            false_alarm_rates.append(sdt_obj.false_alarm_rate())  # Remember that false_alarm_rate() is from SignalDetectionTheory
        # We can also use list comprehension:
        # false_alarm_rates = [sdt_obj.false_alarm_rate() for sdt_obj, _ in self.condition]
        first_element = sorted(false_alarm_rates)
        return first_element





         