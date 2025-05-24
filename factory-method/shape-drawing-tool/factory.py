from __future__ import annotations
from abc import ABC, abstractmethod
from shape import Shape, Circle, Square, Triangle, Hexagon


class Factory(ABC):
    """
    The creator class declares the factory method that is supposed to return an
    object of a Product class. The creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete Shape creators override the factory method in order to change the resulting
product's type.
"""


class CircleFactory(Factory):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> Shape:
        return Circle()

class SquareFactory(Factory):
    def factory_method(self) -> Shape:
        return Square()
    
class TriangleFactory(Factory):
    def factory_method(self) -> Shape:
        return Triangle()
    
class HexagonFactory(Factory):
    def factory_method(self) -> Shape:
        return Hexagon()