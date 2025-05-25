from target import WeatherAPI
from adaptee import WeatherAPI1

class Adapter(WeatherAPI):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via composition.
    """

    def __init__(self, adaptee: WeatherAPI1) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.fetch_weather_data('coords')}"