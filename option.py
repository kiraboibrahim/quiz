from utils.id import AutoID

@AutoID
class Option:
    def __init__(self, value, question):
        self.value = value
        self.question = question
        self.__is_correct = False

    def is_correct(self):
        return self.__is_correct
    
    def set_as_correct_option(self):
        self.__is_correct = True
    
    def __str__(self):
        return self.value
