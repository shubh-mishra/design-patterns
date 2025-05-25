
class WeatherAPI1():
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def fetch_weather_data(self, coords) -> str:
        return "This is Adaptee1 fether_weather_data using coords method"
    
# class WeatherAPI2(Adaptee):
#     """
#     The Adaptee contains some useful behavior, but its interface is incompatible
#     with the existing client code. The Adaptee needs some adaptation before the
#     client code can use it.
#     """

#     def get_weather_data(self, zipcode) -> str:
#         return "This is Adaptee2 get_weather_data using zipcode method"