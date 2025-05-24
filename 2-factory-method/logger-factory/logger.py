from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def operation(self):
        pass

class FileLogger(Logger):

    def operation(self):
        return "This is File logger."

class ConsoleLogger(Logger):

    def operation(self):
        return "This is Console logger."

class DatabaseLogger(Logger):

    def operation(self):
        return "This is Database logger."