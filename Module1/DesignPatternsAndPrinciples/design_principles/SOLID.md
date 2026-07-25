### Single Responsibility Principle (SRP)

##### A class should have only one reason to change
###### _Separate unrelated reasons for change_

```python
class UserRegistration:
    def register(self, username, password):
        # validate + create user

    def save_to_database(self, user):
        # DB-specific code
```

Since registration logic and database logic are in the same class, a change to the database implementation or schema forces us to modify the same class that contains already-working registration logic, unnecessarily increasing the blast radius and risk of regressions.

To fix:
```python
class UserRegistration:
    def register(self, username, password):
        # validate + create user

class UserRepository:
    def save(self, user):
        # DB-specific code
```

### Open/Closed Principle (OCP)

##### A class should be open for extension but closed for modification.
###### _Add new variants without repeatedly changing stable core logic_

```python
class PaymentProcessor:
    def process(self, method, amount):
        if method == "card":
            print("Processing card payment")

        elif method == "upi":
            print("Processing UPI payment")

        elif method == "paypal":       # MODIFY EXISTING CLASS??
```

Existing code may already be used by other parts of the application, so repeatedly modifying it increases the chance of regressions.

If it is expected to grow, design it accordingly to that.

To fix:
```python
class Payment:
    def process(self, amount):
        pass

class CardPayment(Payment):
    def process(self, amount):
        print("Processing card payment")

class UPIPayment(Payment):
    def process(self, amount):
        print("Processing UPI payment")
```


### Liskov Substitution Principle (LSP)
##### Every subclass should be substitutable for its parent class without breaking the expected behaviour of the program

###### _A child must honour the behavioural promises of its parent_

```python
class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")
```

That's biologically correct. But in our software design, Bird makes an additional promise that `Bird → can fly()`, but the Penguin cannot.

Penguin in place of Bird will break the code.

To fix:
```python
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Sparrow(FlyingBird):
    pass

class Penguin(Bird):
    def swim(self):
        print("Swimming")
```

### Interface Segregation Principle (ISP)
##### A class should not be forced to implement methods that it does not need.

###### _Don't make entities do things that they can't_

```python
class Worker:
    def work(self): pass
    def eat(self): pass

class Robot(Worker):
    def work(self):
        print("Working")

    def eat(self):
        raise Exception("I don't eat!")
```

`Robot` needs `work()` but is forced to have `eat()`

To fix:
```python
class Workable:
    def work(self): pass

class Eatable:
    def eat(self): pass

class Robot(Workable):
    def work(self):
        print("Working")
```


### Dependency Inversion Principle (DIP)
##### High-level classes should not depend directly on low-level classes. Both should depend on abstractions.

###### _Do not make classes worry about what's not their business_

```python
class MySQL:
    def save(self):
        print("Saved to MySQL")

class UserService:
    def __init__(self):
        self.db = MySQL()

    def register(self):
        self.db.save()
```

Directly dependent on MySQL only

To fix:
```python
class Database:
    def save(self): pass

class MySQL(Database):
    def save(self):
        print("Saved to MySQL")

class UserService:
    def __init__(self, db: Database):
        self.db = db
```
___ 

:-
```
SRP: Why does this class have to change?
OCP: Does adding a new variant force me to modify stable logic?
LSP: Can this child safely replace its parent?
ISP: Am I forced to depend on methods/capabilities I don't need?
DIP: Am I depending on a concrete implementation when I could depend on an abstraction?
```
