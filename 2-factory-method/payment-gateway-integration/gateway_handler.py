from abc import ABC, abstractmethod

class GatewayHandler(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass

class Stripe(GatewayHandler):
    def operation(self):
        return "This is Stripe gateway handler"
    
class PayPal(GatewayHandler):
    def operation(self):
        return "This is PayPal gateway handler"
    
class RazorPay(GatewayHandler):
    def operation(self):
        return "This is RazorPay gateway handler"