
# 🏭 Factory Pattern – Practice Scenarios

The **Factory Pattern** is a creational design pattern that helps in creating objects without specifying the exact class of the object to be created. Below are practical scenarios to help you practice and reinforce your understanding.

---

## ✅ Recap: What is the Factory Pattern?

- **Purpose**: Encapsulates object creation logic.
- **Problem Solved**: Reduces coupling between code and object instantiation.
- **Key Benefit**: Makes code more flexible and scalable.

---

## 🧪 Practice Scenarios

### 1. 🔵 Shape Drawing Tool

**Description**: Use a factory to return shape objects (`Circle`, `Square`, `Rectangle`) based on input.

```python
shape = ShapeFactory.create_shape("circle")
shape.draw()
```

---

### 2. 🧰 Logger Factory

**Description**: Return a `FileLogger`, `ConsoleLogger`, or `DatabaseLogger` depending on configuration.

```python
logger = LoggerFactory.get_logger("file")
logger.log("Saving data to file")
```

---

### 3. 🧩 Notification System

**Description**: Send notifications via Email, SMS, or Push.

```python
notifier = NotificationFactory.get_notifier("email")
notifier.send("Hello there!")
```

---

### 4. 💳 Payment Gateway Integration

**Description**: Return the correct payment gateway handler like Stripe, PayPal, or Razorpay.

```python
payment = PaymentGatewayFactory.get_gateway("stripe")
payment.charge(500)
```

---

### 5. 📁 Document Parser

**Description**: A parser for reading files like PDF, DOCX, or TXT.

```python
parser = ParserFactory.get_parser("pdf")
parser.parse("/path/to/file.pdf")
```

---

### 6. 🧙 Game Character Creator

**Description**: Create a character like Knight, Archer, or Mage using a factory.

```python
character = CharacterFactory.create_character("mage")
character.attack()
```

---

## 🧠 Self-Check: Have You Mastered It?

- ✅ Can you dynamically choose classes at runtime?
- ✅ Is your object creation logic decoupled from its usage?
- ✅ Can you add new types without changing the factory interface?
- ✅ Do all products share a common interface?
- ✅ Can you mock or swap components easily?

If your answer is **yes** to all – you're doing great!

---

## 📚 Resources

- [Refactoring Guru – Factory Pattern](https://refactoring.guru/design-patterns/factory-method)
- [Real Python – Factory Pattern](https://realpython.com/factory-method-python/)
