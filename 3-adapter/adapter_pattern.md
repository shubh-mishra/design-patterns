
# 🔌 Adapter Pattern – Practice Scenarios

The **Adapter Pattern** is a structural design pattern that allows incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces.

---

## ✅ Recap: What is the Adapter Pattern?

- **Purpose**: Convert the interface of a class into another interface clients expect.
- **Problem Solved**: When you want to reuse existing code but its interface is incompatible with the code you're working with.
- **Key Benefit**: Promotes code reusability and compatibility without modifying existing code.

---

## 🧪 Practice Scenarios

### 1. 🖨️ Legacy Printer API Adapter

**Description**: You have a new system that expects a `print_document()` method, but a legacy printer API only supports `send_to_printer(doc)`.

**Practice**: Write an adapter that wraps the old API and provides the expected `print_document()` interface.

---

### 2. 🌐 External Weather API Adapter

**Description**: Your app uses a `get_temperature(location)` method, but a new weather service uses `fetch_weather_data(coords)`.

**Practice**: Build an adapter that translates between your interface and the new API.

---

### 3. 🔌 Power Plug Adapter

**Description**: Simulate an electrical plug system where different countries use different socket types. Design an adapter that lets European plugs fit into American sockets.

**Practice**: Great for simulating real-world physical adapters in code.

---

### 4. 🎮 Game Controller Adapter

**Description**: A game engine expects a `Controller` interface, but you want to plug in third-party hardware with a different interface.

**Practice**: Create an adapter that maps the hardware inputs to the expected `Controller` methods.

---

### 5. 📦 Payment Gateway Adapter

**Description**: Your e-commerce platform supports a standard `process_payment(amount)` interface, but different gateways (Stripe, PayPal, etc.) have different method names.

**Practice**: Implement adapters to allow easy switching or extension of payment providers.

---

### 6. 🎥 Media Player Adapter

**Description**: A media player supports `play(file_type, file_name)`, but you want to add support for a new video format with a different library.

**Practice**: Use an adapter to connect the new video library to the existing player interface.

---

## 🧠 Self-Check: Have You Mastered It?

- ✅ Can you identify when two interfaces are incompatible?
- ✅ Are you able to create an adapter that maps one interface to another?
- ✅ Do you understand that the original classes stay unchanged?
- ✅ Are you comfortable using both object and class adapters (via inheritance and composition)?

If your answer is **yes** to all – you're on the right track!

---

## 📚 Resources

- [Refactoring Guru – Adapter Pattern](https://refactoring.guru/design-patterns/adapter)
- [Real Python – Adapter Pattern in Python](https://realpython.com/adapter-pattern-python/)
