class WeatherAPI:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def get_temperature(self, location) -> str:
        return "Target: The default target's behavior using get_temperature with location method"