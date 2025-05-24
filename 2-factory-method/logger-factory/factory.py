from abc import ABC, abstractmethod
from logger import Logger, FileLogger, ConsoleLogger, DatabaseLogger

class Factory(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):

        product = self.factory_method()

        result = product.operation()

        return result

class FileLoggerFactory(Factory):

    def factory_method(self) -> Logger:
        return FileLogger()
    
class ConsoleLoggerFactory(Factory):

    def factory_method(self) -> Logger:
        return ConsoleLogger()
    
class DatabaseLoggerFactory(Factory):

    def factory_method(self) -> Logger:
        return DatabaseLogger()