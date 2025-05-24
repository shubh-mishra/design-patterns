from __future__ import annotations
from abc import ABC, abstractmethod

class Shape(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class Circle(Shape):
    def operation(self) -> str:
        return "{Result of the Circle}"


class Square(Shape):
    def operation(self) -> str:
        return "{Result of the Square}"
    
class Triangle(Shape):
    def operation(self) -> str:
        return "{Result of the Triangle}"
    
class Hexagon(Shape):
    def operation(self) -> str:
        return "{Result of the Hexagon}"