from abc import ABCMeta
from abc import abstractmethod

class Exchange(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def get_amount_invested(self):
        return 0

if __name__ == '__main__':
    print("Hello World")
