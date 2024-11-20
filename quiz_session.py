from datetime import datetime, timedelta
from exceptions import QuizSessionTimedOutException, ClosedQuizSessionException, PendingQuizSessionException, ClosedQuizException
from utils.id import AutoID

from quiz import Quiz
from question import SingleChoiceQuestion
from option import Option
from student import Student

@AutoID
class QuizSession:
    PENDING = 1
    CLOSED = 4
    OPEN = 2

    def __init__(self, student, quiz):
        if(quiz.is_closed()):
            raise ClosedQuizException(quiz)
        
        self.__student = student
        self.__status = QuizSession.PENDING
        self.__quiz = quiz
        self.__question_pointer = 0
        self.__started_at = None
        self.__ends_at = None
        self.__answer_sheet = {
            "student": self.__student,
            "answers": {}
        }

    @property
    def remaining_time(self):
        try:
            self.__handleDisabledState()
        except QuizSessionTimedOutException:
            return 0
        now = datetime.now()
        time_diff = now - self.__ends_at
        return time_diff.total_seconds()
    
    def open(self):
        try:
            self.__handleDisabledState()
        except PendingQuizSessionException:
            self.__status = QuizSession.OPEN
            self.__started_at = datetime.now()
            self.__ends_at = self.__started_at + timedelta(minutes=self.__quiz.duration)
            return self.goto_question(0)
        
    def is_pending(self):
        return self.__status == QuizSession.PENDING
    
    def is_closed(self):
        return self.__status == QuizSession.CLOSED
    
    def is_open(self):
        return self.__status == QuizSession.OPEN
    
    def is_timed_out(self):
        now = datetime.now()
        return now > self.__ends_at

    def get_previous_question(self):
        self.__question_pointer -= 1
        return self.goto_question(self.__question_pointer)
    
    def get_next_question(self):
        self.__question_pointer += 1
        return self.goto_question(self.__question_pointer)
    
    def goto_question(self, question_number):
        self.__handleDisabledState()
        # Question pointer uses zero based indexing and yet the question_number used one based indexing
        self.__question_pointer = question_number
        return self.quiz.get_question(self.__question_pointer)
    
    def close(self):
        self.__status = QuizSession.CLOSED

    def submit(self):
        self.__handleDisabledState()
        # Close quiz session and return user's answers
        self.close()
        return self.__answer_sheet


    def save_option(self, option):
        self.__handleDisabledState()
        current_question = self.goto_question(self.__question_pointer)
        self.__answer_sheet["answers"][current_question.id] = option
    
    def __handleDisabledState(self):
        """
        A wrapper around the three inactive states of a quiz session: closed, pending, and timed_out
        Raise a ClosedQuizSessionException when the quiz to be attempted is closed, or raise a PendingQuizSessionException
        when quiz session is in a pending state or raise a QuizSessionTimedOutException when a quiz
        session is timed out
        """
        if(self.is_pending()):
            raise PendingQuizSessionException()
        elif(self.is_timed_out()):
            self.close()
            raise QuizSessionTimedOutException()
        elif(self.is_closed()):
            raise ClosedQuizSessionException()


question = SingleChoiceQuestion()
OPTIONS = [
    Option("A", )
]
oop_quiz = Quiz()