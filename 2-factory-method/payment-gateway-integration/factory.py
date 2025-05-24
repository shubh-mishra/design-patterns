from abc import ABC, abstractmethod
from gateway_handler import GatewayHandler, Stripe, PayPal, RazorPay

class Factory(ABC):

    @abstractmethod
    def factory_method(self):
        None

    def some_operation(self):
        product = self.factory_method()
        result = product.operation()
        return result
    
class StripeFactory(Factory):
    def factory_method(self) -> GatewayHandler:
        return Stripe()
    
class PayPalFactory(Factory):
    def factory_method(self) -> GatewayHandler:
        return PayPal()
    
class RazorPayFactory(Factory):
    def factory_method(self) -> GatewayHandler:
        return RazorPay()