import functools

def AutoID(cls):
    """
    A Decorator that adds an auto incrementing unique ID for each instance of the class created
    """
    @functools.wraps(cls, updated=())
    class Wrapper(cls):
        __id_generator = None

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        @property
        def id(self):
            if(not hasattr(self, "__id")):
                self.__id = self.__get_id()
            return self.__id

        @classmethod
        def __get_id(cls):
            # Maintian a single generator per all instances of the class
            if cls.__id_generator is None:
                cls.__id_generator = cls.__get_id_generator()
            return next(cls.__id_generator)
        
        @staticmethod
        def __get_id_generator():
            id = 1
            while True:
                yield id
                id += 1

    return Wrapper

@AutoID
class Student:
    def __init__(self, name):
        self.name = name

@AutoID
class Employee:
    def __init__(self, name):
        self.name = name

s1 = Student("Loora")
s2 = Student("Kirabo Ibrahim")
s3 = Student("Kirabo Ibrahim")
e1 = Employee("MIkey Bee")

print(s1.id, s2.id, s3.id, e1.id)