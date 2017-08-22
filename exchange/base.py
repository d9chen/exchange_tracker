from abc import ABCMeta
from abc import abstractmethod

class AbstractExchange(metaclass=ABCMeta):

    @abstractmethod
    def get_amount_invested(self):
        pass

class DummyExchange(AbstractExchange):

    def get_amount_invested(self):
        return 0
