class ClosedQuizException(Exception):
    def __init__(self, quiz):
        message = "Quiz is closed"
        super().__init__(message)

class QuizSessionTimedOutException(Exception):
    def __init__(self):
        message = "Quiz session timed out"
        super().__init__(message)


class ClosedQuizSessionException(Exception):
    pass

class PendingQuizSessionException(Exception):
    pass