from abc import ABC, abstractmethod

class Character(ABC):

    @abstractmethod
    def operation(self):
        pass

class Knight(Character):
    
    def operation(self):
        return "This is Knight Character."
    
class Mage(Character):
    
    def operation(self):
        return "This is Mage Character."
    
class Archer(Character):
    
    def operation(self):
        return "This is Archer Character."