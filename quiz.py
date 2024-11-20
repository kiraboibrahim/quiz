from datetime import datetime
from utils.id import AutoID

@AutoID
class Quiz:
    CLOSED = 'CLOSED'
    OPEN = 'OPEN'

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.questions = []
        self.created_at = datetime.now()
        self.__status = Quiz.CLOSED

    def get_question(self, index):
        if(index < self.num_questions):
            return self.questions[index]
        return None
    
    @property
    def num_questions(self):
        return len(self.questions)
     
    def open(self):
        self.__status = Quiz.OPEN
    
    def close(self):
        self.__status = Quiz.CLOSED

    def is_closed(self):
        return self.__status == Quiz.CLOSED
    
    def is_open(self):
        return self.__status == Quiz.OPEN
    
    def add_question(self, question):
        self.questions.append(question)

    def delete_question(self, question):
        self.questions.remove(question)

    def grade(self):
        score = 0
        for question in self.questions:
            if(question.is_passed()):
                score += 1
        return (score / self.num_questions) * 100
