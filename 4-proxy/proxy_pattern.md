
# 🛡️ Proxy Pattern – Practice Scenarios

The **Proxy Pattern** is a structural design pattern that provides a **placeholder or surrogate** for another object to control access to it.

---

## ✅ Recap: What is the Proxy Pattern?

- **Purpose**: Control access to an object, add additional behavior, or manage resource-intensive operations.
- **Common Types**:
  - **Virtual Proxy**: Delay the creation of expensive objects until needed.
  - **Protection Proxy**: Control access based on permissions.
  - **Remote Proxy**: Represent an object in a different address space (e.g., over network).
  - **Logging/Caching Proxy**: Add extra functionality like logging or caching without modifying the real object.

---

## 🧪 Practice Scenarios

### 1. 🖼️ Lazy Image Loader (Virtual Proxy)

**Description**: Only load an image file from disk when it's actually displayed.

```python
class Image:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")

class ProxyImage:
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = Image(self.filename)
        self.real_image.display()
```

---

### 2. 🔐 Protected File Access (Protection Proxy)

**Description**: Only allow users with specific roles to access certain files.

```python
class FileAccessor:
    def read(self):
        print("Reading file...")

class ProtectedFileProxy:
    def __init__(self, user_role):
        self.user_role = user_role
        self.accessor = FileAccessor()

    def read(self):
        if self.user_role != "admin":
            print("Access Denied!")
        else:
            self.accessor.read()
```

---

### 3. 🧠 Heavy NLP Model (Virtual Proxy)

**Description**: A large NLP model takes time and memory to load. Only load it if a function actually needs it.

```python
class NLPModel:
    def __init__(self):
        print("Loading large NLP model...")

    def analyze(self, text):
        print(f"Analyzing text: {text}")

class NLPProxy:
    def __init__(self):
        self.model = None

    def analyze(self, text):
        if self.model is None:
            self.model = NLPModel()
        self.model.analyze(text)
```

---

### 4. 📝 Logging Proxy

**Description**: Log every interaction with a data service.

```python
class DataService:
    def get_data(self):
        return "some data"

class LoggingProxy:
    def __init__(self, target):
        self.target = target

    def get_data(self):
        print("Log: get_data() called")
        return self.target.get_data()
```

---

## 🧠 Self-Check: Have You Mastered It?

- ✅ Can you intercept method calls using a proxy object?
- ✅ Do you understand when to load/defer/delegate to the real object?
- ✅ Are you comfortable applying proxy in security, performance, and access scenarios?

If your answer is **yes** to all – you’ve got it!

---

## 📚 Resources

- [Refactoring Guru – Proxy Pattern](https://refactoring.guru/design-patterns/proxy)
- [Real Python – Proxy Pattern](https://realpython.com/primer-on-python-decorators/#building-a-logging-decorator)
