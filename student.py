from utils.id import AutoID
from quiz_session import QuizSession


@AutoID
class Student:
    def __init__(self, first_name, last_name, reg_no,):
        self.first_name = first_name
        self.last_name = last_name
        self.reg_no = reg_no
    
    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"
    
    def take_quiz(self, quiz):
        return QuizSession(self, quiz)
