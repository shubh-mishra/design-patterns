from factory import Factory, StripeFactory, PayPalFactory

def client_code(creator: Factory) -> None:
    result = creator.some_operation()
    print(result)

if __name__ == "__main__":
    print("Lanching from StripeFactory")
    client_code(StripeFactory())
    print("\n")

    print("Lanching from PayPalFactory")
    client_code(PayPalFactory())
    print("\n")