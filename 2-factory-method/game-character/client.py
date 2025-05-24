from factory import Factory, MageFactory, KnightFactory

def client_code(creator: Factory):

    result = creator.some_operation()
    print(result)

if __name__ == "__main__":
    print("Launching Knight character")
    client_code(KnightFactory())

    print("Launching Mage character")
    client_code(MageFactory())