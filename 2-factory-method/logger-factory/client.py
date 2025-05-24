from factory import Factory, FileLoggerFactory, ConsoleLoggerFactory

def client_code(creator: Factory):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the FileLoggerFactory.")
    client_code(FileLoggerFactory())
    print("\n")

    print("App: Launched with the ConsoleLoggerFactory.")
    client_code(ConsoleLoggerFactory())