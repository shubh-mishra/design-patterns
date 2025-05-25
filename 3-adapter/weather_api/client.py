from target import WeatherAPI
from adaptee import WeatherAPI1
from adapter import Adapter

def client_code(target: WeatherAPI) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.get_temperature("location"), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = WeatherAPI()
    client_code(target)
    print("\n")

    adaptee = WeatherAPI1()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.fetch_weather_data('coords')}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)