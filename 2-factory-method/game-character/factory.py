from abc import ABC, abstractmethod
from character import Character, Knight, Mage, Archer


class Factory(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = product.operation()
        return result
    
class KnightFactory(Factory):
    def factory_method(self) -> Character:
        return Knight()
    

class MageFactory(Factory):
    def factory_method(self) -> Character:
        return Mage()
    

class ArcherFactory(Factory):
    def factory_method(self) -> Character:
        return Archer()