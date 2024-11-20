from utils.id import AutoID


@AutoID
class SingleChoiceQuestion:
    def __init__(self, text, quiz):
        self.text = text
        self.options = []
        self.set_quiz(quiz)
    
    def set_quiz(self, quiz):
        quiz.add_question(self)
        self.quiz = quiz
    
    def delete(self):
        self.quiz.delete_question(self)

    def is_passed(self, option):
        # Sometimes, the student may not have answered the question, and in this case, the option
        # will be None 
        return False if option is None else option.is_correct()
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return self.text


class MultipleChoiceQuestion(SingleChoiceQuestion):
    def __init__(self, text, quiz):
        super().__init__(text, quiz)
    
    def is_passed(self, *options):
        return False if len(options) == 0 else all(option.is_correct() for option in options)