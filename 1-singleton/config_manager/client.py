from singleton import ConfigManager

if __name__ == "__main__":
    # The client code.

    s1 = ConfigManager()
    s2 = ConfigManager()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")