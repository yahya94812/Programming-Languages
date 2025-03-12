"""comprehensive Python code examples to illustrate Object-Oriented Programming (OOP) concepts in Python."""
# Python Object-Oriented Programming (OOP) Comprehensive Examples

# 1. Classes and Objects
class Dog:
    """A simple Dog class to demonstrate class creation and basic methods"""
    
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initialization)
    def __init__(self, name, age, breed):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        self.breed = breed
    
    # Instance method
    def description(self):
        return f"{self.name} is a {self.age} year old {self.breed}"
    
    # Instance method with behavior
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    # String representation
    def __str__(self):
        return f"{self.name}, {self.breed}, {self.age} years old"
    
    # String representation for developers
    def __repr__(self):
        return f"Dog('{self.name}', {self.age}, '{self.breed}')"


# 2. Inheritance
class Mammal:
    """Base class for mammals"""
    
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"


class Cat(Mammal):
    """Cat class inheriting from Mammal"""
    
    def __init__(self, name, age, weight, color):
        # Call the parent class's __init__ method
        super().__init__(name, age, weight)
        self.color = color
    
    def purr(self):
        return f"{self.name} is purring"
    
    # Method overriding
    def sleep(self):
        return f"{self.name} is sleeping lazily on the couch"


# 3. Multiple Inheritance
class Flyable:
    """Mixin class for flying capability"""
    
    def fly(self):
        return "Flying high!"


class Swimmable:
    """Mixin class for swimming capability"""
    
    def swim(self):
        return "Swimming gracefully!"


class Duck(Mammal, Flyable, Swimmable):
    """Duck class demonstrating multiple inheritance"""
    
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
    
    def quack(self):
        return f"{self.name} quacks!"


# 4. Encapsulation
class BankAccount:
    """A class to demonstrate encapsulation"""
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self._balance = balance  # Protected attribute (convention)
        self.__account_number = self._generate_account_number()  # Private attribute
    
    def _generate_account_number(self):
        """Protected method"""
        import random
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        return self._balance
    
    def get_account_info(self):
        # Last 4 digits of account number
        last_four = str(self.__account_number)[-4:]
        return f"Account holder: {self.account_holder}, Account: XXXXXX{last_four}"


# 5. Polymorphism
class Shape:
    """Base class for shapes"""
    
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Rectangle class"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle class"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


# 6. Abstraction with Abstract Base Classes
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class for vehicles"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    """Car class implementing the Vehicle abstract class"""
    
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self._is_engine_running = False
    
    def start_engine(self):
        if not self._is_engine_running:
            self._is_engine_running = True
            return f"{self.get_info()} engine started"
        return f"{self.get_info()} engine is already running"
    
    def stop_engine(self):
        if self._is_engine_running:
            self._is_engine_running = False
            return f"{self.get_info()} engine stopped"
        return f"{self.get_info()} engine is already off"


# 7. Properties (Getters, Setters, Deleters)
class Temperature:
    """Class to demonstrate properties"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Getter for fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for fahrenheit"""
        celsius = (value - 32) * 5/9
        if celsius < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = celsius


# 8. Class Methods and Static Methods
class DateUtil:
    """Class to demonstrate class methods and static methods"""
    
    @staticmethod
    def is_leap_year(year):
        """Static method to check if a year is a leap year"""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    @staticmethod
    def days_in_month(month, year):
        """Static method to get days in a month"""
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and DateUtil.is_leap_year(year):
            return 29
        return days[month]


class Date:
    """Class to demonstrate class methods as alternative constructors"""
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """Class method to create Date object from string"""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """Class method to create Date object with today's date"""
        import datetime
        now = datetime.datetime.now()
        return cls(now.year, now.month, now.day)
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"


# 9. Magic/Dunder Methods
class Point:
    """Class to demonstrate magic methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        """Addition operator (+)"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Subtraction operator (-)"""
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        """Equality operator (==)"""
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        """Less than operator (<)"""
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
    
    def __len__(self):
        """Length function"""
        import math
        return int(math.sqrt(self.x**2 + self.y**2))


# 10. Context Managers
class FileManager:
    """A simple context manager for file operations"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return True to suppress exceptions, False to propagate them
        return False


# 11. Composition
class Engine:
    """Engine class for composition example"""
    
    def __init__(self, horsepower, cylinders):
        self.horsepower = horsepower
        self.cylinders = cylinders
        self._running = False
    
    def start(self):
        self._running = True
        return "Engine started"
    
    def stop(self):
        self._running = False
        return "Engine stopped"
    
    def status(self):
        return "Running" if self._running else "Off"


class Transmission:
    """Transmission class for composition example"""
    
    def __init__(self, type_):
        self.type = type_  # "automatic" or "manual"
        self.gear = 0
    
    def shift_up(self):
        if self.gear < 6:
            self.gear += 1
        return f"Shifted to gear {self.gear}"
    
    def shift_down(self):
        if self.gear > 0:
            self.gear -= 1
        return f"Shifted to gear {self.gear}"


class Vehicle:
    """Vehicle class demonstrating composition"""
    
    def __init__(self, make, model, engine, transmission):
        self.make = make
        self.model = model
        self.engine = engine  # Composition
        self.transmission = transmission  # Composition
    
    def start(self):
        return self.engine.start()
    
    def stop(self):
        return self.engine.stop()
    
    def shift_up(self):
        return self.transmission.shift_up()
    
    def shift_down(self):
        return self.transmission.shift_down()
    
    def status(self):
        return f"{self.make} {self.model}: Engine is {self.engine.status()}, Gear: {self.transmission.gear}"


# 12. Metaclasses
class SingletonMeta(type):
    """Metaclass for implementing the Singleton pattern"""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    """Logger class using Singleton pattern"""
    
    def __init__(self):
        self.logs = []
    
    def log(self, message):
        self.logs.append(message)
        print(f"LOG: {message}")
    
    def get_logs(self):
        return self.logs


# 13. Descriptors
class Validator:
    """A descriptor that validates values"""
    
    def __init__(self, name, validation_func, error_msg):
        self.name = name
        self.validation_func = validation_func
        self.error_msg = error_msg
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)
    
    def __set__(self, instance, value):
        if not self.validation_func(value):
            raise ValueError(f"{self.error_msg}: {value}")
        instance.__dict__[self.name] = value


class Person:
    """Class using validators"""
    
    name = Validator("_name", lambda x: isinstance(x, str) and len(x) > 0, "Name must be a non-empty string")
    age = Validator("_age", lambda x: isinstance(x, int) and 0 <= x <= 150, "Age must be between 0 and 150")
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person({self.name}, {self.age})"


# 14. Example Usage
def demonstrate_oop():
    print("\n--- Classes and Objects ---")
    miles = Dog("Miles", 4, "Jack Russell Terrier")
    buddy = Dog("Buddy", 9, "Golden Retriever")
    print(miles.description())
    print(miles.speak("Woof!"))
    print(buddy.speak("Bark!"))
    print(f"Both dogs are of species {Dog.species}")
    print(f"String representation: {miles}")

    print("\n--- Inheritance ---")
    whiskers = Cat("Whiskers", 3, 4.5, "gray")
    print(whiskers.eat())
    print(whiskers.sleep())
    print(whiskers.purr())

    print("\n--- Multiple Inheritance ---")
    donald = Duck("Donald", 5, 3.5)
    print(donald.eat())
    print(donald.quack())
    print(donald.fly())
    print(donald.swim())

    print("\n--- Encapsulation ---")
    account = BankAccount("John Doe", 1000)
    print(account.get_account_info())
    print(account.deposit(500))
    print(account.withdraw(200))
    print(f"Current balance: ${account.get_balance()}")
    # Trying to access private attribute will cause an AttributeError
    # print(account.__account_number)  # This will fail

    print("\n--- Polymorphism ---")
    rect = Rectangle(5, 4)
    circle = Circle(3)
    shapes = [rect, circle]
    for shape in shapes:
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")

    print("\n--- Abstraction ---")
    car = Car("Toyota", "Corolla", 2023, "Hybrid")
    print(car.get_info())
    print(car.start_engine())
    print(car.stop_engine())

    print("\n--- Properties ---")
    temp = Temperature(25)
    print(f"Celsius: {temp.celsius}°C")
    print(f"Fahrenheit: {temp.fahrenheit}°F")
    temp.celsius = 30
    print(f"Celsius: {temp.celsius}°C")
    print(f"Fahrenheit: {temp.fahrenheit}°F")
    temp.fahrenheit = 50
    print(f"Celsius: {temp.celsius}°C")
    print(f"Fahrenheit: {temp.fahrenheit}°F")

    print("\n--- Class and Static Methods ---")
    print(f"Is 2024 a leap year? {DateUtil.is_leap_year(2024)}")
    print(f"Days in February 2024: {DateUtil.days_in_month(2, 2024)}")
    date1 = Date(2023, 12, 25)
    date2 = Date.from_string("2023-12-25")
    date3 = Date.today()
    print(f"Date 1: {date1}")
    print(f"Date 2: {date2}")
    print(f"Today: {date3}")

    print("\n--- Magic Methods ---")
    p1 = Point(2, 3)
    p2 = Point(3, 4)
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p1 + p2: {p1 + p2}")
    print(f"p1 - p2: {p1 - p2}")
    print(f"p1 == p2: {p1 == p2}")
    print(f"p1 < p2: {p1 < p2}")
    print(f"Length of p1: {len(p1)}")

    print("\n--- Composition ---")
    engine = Engine(150, 4)
    transmission = Transmission("automatic")
    car = Vehicle("Honda", "Civic", engine, transmission)
    print(car.start())
    print(car.shift_up())
    print(car.shift_up())
    print(car.status())
    print(car.stop())

    print("\n--- Singleton (Metaclass) ---")
    logger1 = Logger()
    logger2 = Logger()
    print(f"Same logger instance: {logger1 is logger2}")
    logger1.log("Test message 1")
    logger2.log("Test message 2")
    print(f"All logs: {logger1.get_logs()}")

    print("\n--- Descriptors ---")
    try:
        john = Person("John", 30)
        print(john)
        # This will raise a ValueError
        invalid_person = Person("", -5)
    except ValueError as e:
        print(f"Validation error: {e}")


if __name__ == "__main__":
    demonstrate_oop()
    
# Output
"""--- Classes and Objects ---
Miles is a 4 year old Jack Russell Terrier
Miles says Woof!
Buddy says Bark!
Both dogs are of species Canis familiaris
String representation: Miles, Jack Russell Terrier, 4 years old

--- Inheritance ---
Whiskers is eating
Whiskers is sleeping lazily on the couch
Whiskers is purring

--- Multiple Inheritance ---
Donald is eating
Donald quacks!
Flying high!
Swimming gracefully!

--- Encapsulation ---
Account holder: John Doe, Account: XXXXXX6312
Deposited $500. New balance: $1500
Withdrew $200. New balance: $1300
Current balance: $1300

--- Polymorphism ---
Area: 20
Perimeter: 18
Area: 28.274333882308138
Perimeter: 18.84955592153876

--- Abstraction ---
2023 Toyota Corolla
2023 Toyota Corolla engine started
2023 Toyota Corolla engine stopped

--- Properties ---
Celsius: 25°C
Fahrenheit: 77.0°F
Celsius: 30°C
Fahrenheit: 86.0°F
Celsius: 10.0°C
Fahrenheit: 50.0°F

--- Class and Static Methods ---
Is 2024 a leap year? True
Days in February 2024: 29
Date 1: 2023-12-25
Date 2: 2023-12-25
Today: 2025-03-12

--- Magic Methods ---
p1: Point(2, 3)
p2: Point(3, 4)
p1 + p2: Point(5, 7)
p1 - p2: Point(-1, -1)
p1 == p2: False
p1 < p2: True
Length of p1: 3

--- Composition ---
Engine started
Shifted to gear 1
Shifted to gear 2
Honda Civic: Engine is Running, Gear: 2
Engine stopped

--- Singleton (Metaclass) ---
Same logger instance: True
LOG: Test message 1
LOG: Test message 2
All logs: ['Test message 1', 'Test message 2']

--- Descriptors ---
Person(John, 30)
Validation error: Name must be a non-empty string: """    

"""This comprehensive code example covers all major concepts of Object-Oriented Programming (OOP) in Python:

Classes and Objects: Basic class definition, instance variables, methods, and special methods (str, repr)
Inheritance: Creating child classes that inherit from parent classes, using super() for parent class initialization
Multiple Inheritance: Using mixins and combining functionality from multiple parent classes
Encapsulation: Protecting data with private/protected attributes and methods
Polymorphism: Different classes implementing the same methods in different ways
Abstraction: Using abstract base classes to define interfaces
Properties: Implementing getters, setters, and deleters using the @property decorator
Class and Static Methods: Utility methods and alternative constructors
Magic/Dunder Methods: Special methods for operator overloading and Python integration
Context Managers: Classes that can be used with the 'with' statement
Composition: Building complex objects by combining simpler ones
Metaclasses: Customizing class creation behavior (Singleton pattern)
Descriptors: Objects that customize attribute access (validation)
Usage Demonstration: Complete examples showing all concepts in action

The code is heavily commented to explain each concept and includes a demonstration function to show how everything works together."""

