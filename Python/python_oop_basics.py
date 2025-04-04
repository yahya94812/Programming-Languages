# Python Object-Oriented Programming (OOP) Basics Tutorial

# 1. Classes and Objects
print("1. Classes and Objects")
print("-" * 50)

class Car:
    """
    A simple Car class demonstrating the basic structure of a class
    """
    # Class attribute (shared by all instances)
    wheels = 4
    
    # Constructor (initializer method)
    def __init__(self, make, model, year, color):
        # Instance attributes (unique to each instance)
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer = 0  # default value
        
    # Instance method
    def drive(self, miles):
        self.odometer += miles
        return f"{self.make} {self.model} has driven {miles} miles"
    
    # Another instance method
    def get_description(self):
        return f"{self.year} {self.color} {self.make} {self.model}"
    
    # String representation method
    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
    
    # Representation method (for developers/debugging)
    def __repr__(self):
        return f"Car('{self.make}', '{self.model}', {self.year}, '{self.color}')"

# Creating objects (instances of the Car class)
my_car = Car("Toyota", "Corolla", 2020, "Blue")
your_car = Car("Honda", "Civic", 2019, "Red")

# Accessing attributes and methods
print(f"My car: {my_car}")
print(f"Your car: {your_car}")
print(f"My car's description: {my_car.get_description()}")
print(f"Class attribute: All cars have {Car.wheels} wheels")
print(f"Instance attribute: My car's odometer: {my_car.odometer}")
print(my_car.drive(100))
print(f"Updated odometer: {my_car.odometer}")
print(f"Developer representation: {repr(my_car)}")
print()

# 2. Encapsulation
print("2. Encapsulation")
print("-" * 50)

class BankAccount:
    """
    A BankAccount class demonstrating encapsulation
    """
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        # Private attribute (convention: starts with _)
        self._balance = balance
        # Double underscore makes it harder to access directly (name mangling)
        self.__transaction_log = []
        
    # Getter method
    def get_balance(self):
        return self._balance
    
    # Setter method
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            self.__log_transaction("set_balance", amount)
        else:
            raise ValueError("Balance cannot be negative")
    
    # Property decorator - combines getter and setter
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
            self.__log_transaction("balance_update", amount)
        else:
            raise ValueError("Balance cannot be negative")
    
    # Public methods
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__log_transaction("deposit", amount)
            return f"Deposited ${amount}. New balance: ${self._balance}"
        else:
            raise ValueError("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__log_transaction("withdrawal", amount)
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        else:
            raise ValueError("Invalid withdrawal amount")
    
    # Private method (convention: starts with _)
    def __log_transaction(self, transaction_type, amount):
        import datetime
        timestamp = datetime.datetime.now()
        self.__transaction_log.append(f"{timestamp}: {transaction_type} - ${amount}")
    
    # Method to reveal the "private" transaction log
    def get_transaction_history(self):
        return self.__transaction_log

# Using the BankAccount class
account = BankAccount("12345", "John Doe", 1000)
print(f"Account owner: {account.owner_name}")
print(f"Initial balance: ${account.get_balance()}")
print(account.deposit(500))
print(account.withdraw(200))

# Using property
print(f"Balance via property: ${account.balance}")
account.balance = 2000
print(f"New balance via property: ${account.balance}")

try:
    account.balance = -100  # This will raise an error
except ValueError as e:
    print(f"Error: {e}")

# Accessing transaction history
print("Transaction history:")
for transaction in account.get_transaction_history():
    print(f"  {transaction}")

# Trying to access "private" attributes
try:
    print(account._balance)  # Convention-based private attribute (still accessible)
    # print(account.__transaction_log)  # This would raise an AttributeError
    # But we can still access it if we know the name mangling pattern
    print(account._BankAccount__transaction_log)  # This works but is discouraged
except AttributeError as e:
    print(f"Error: {e}")
print()

# 3. Inheritance
print("3. Inheritance")
print("-" * 50)

class Vehicle:
    """Base Vehicle class"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        self.is_running = True
        return f"{self.make} {self.model} started"
    
    def stop(self):
        self.is_running = False
        return f"{self.make} {self.model} stopped"
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricVehicle(Vehicle):
    """Electric Vehicle class inheriting from Vehicle"""
    def __init__(self, make, model, year, battery_capacity):
        # Call the parent class constructor
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.battery_level = 100
    
    # Override the parent class method
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} (Electric - {self.battery_capacity} kWh)"
    
    # Add a new method
    def charge(self):
        self.battery_level = 100
        return f"{self.make} {self.model} charged to {self.battery_level}%"

class HybridVehicle(Vehicle):
    """Hybrid Vehicle class inheriting from Vehicle"""
    def __init__(self, make, model, year, battery_capacity, fuel_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.fuel_capacity = fuel_capacity
        self.battery_level = 100
        self.fuel_level = 100
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} (Hybrid - {self.battery_capacity} kWh, {self.fuel_capacity} gal)"

# Create instances of different vehicle types
regular_car = Vehicle("Toyota", "Camry", 2021)
electric_car = ElectricVehicle("Tesla", "Model 3", 2022, 75)
hybrid_car = HybridVehicle("Toyota", "Prius", 2020, 8.8, 11.3)

# Test Vehicle features
print(f"Regular car: {regular_car.get_info()}")
print(regular_car.start())

# Test ElectricVehicle features
print(f"Electric car: {electric_car.get_info()}")
print(electric_car.start())  # Inherited method
print(electric_car.charge())  # New method

# Test HybridVehicle features
print(f"Hybrid car: {hybrid_car.get_info()}")
print()

# 4. Polymorphism
print("4. Polymorphism")
print("-" * 50)

def start_vehicle(vehicle):
    """Function that works with any vehicle type"""
    # Polymorphism through a common interface
    vehicle_info = vehicle.get_info()
    start_message = vehicle.start()
    return f"Starting: {vehicle_info}\n{start_message}"

# Call the same function with different types of vehicles
print(start_vehicle(regular_car))
print(start_vehicle(electric_car))
print(start_vehicle(hybrid_car))

# Polymorphism with different classes
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Using polymorphism
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
print()

# 5. Abstraction
print("5. Abstraction")
print("-" * 50)

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract class for payment processing"""
    
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def refund_payment(self, amount):
        pass
    
    # Concrete method that all subclasses will inherit
    def verify_payment(self, amount):
        return amount > 0

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number, expiry_date):
        self.card_number = card_number
        self.expiry_date = expiry_date
    
    def process_payment(self, amount):
        if self.verify_payment(amount):
            return f"Processed ${amount} payment with credit card ending in {self.card_number[-4:]}"
        return "Invalid payment amount"
    
    def refund_payment(self, amount):
        return f"Refunded ${amount} to credit card ending in {self.card_number[-4:]}"

class PayPalProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email
    
    def process_payment(self, amount):
        if self.verify_payment(amount):
            return f"Processed ${amount} payment with PayPal account: {self.email}"
        return "Invalid payment amount"
    
    def refund_payment(self, amount):
        return f"Refunded ${amount} to PayPal account: {self.email}"

# Using abstraction
cc_processor = CreditCardProcessor("1234-5678-9012-3456", "12/25")
paypal_processor = PayPalProcessor("user@example.com")

print(cc_processor.process_payment(100))
print(paypal_processor.process_payment(50))
print(cc_processor.refund_payment(25))
print()

# 6. Multiple Inheritance
print("6. Multiple Inheritance")
print("-" * 50)

class Engine:
    def __init__(self, power):
        self.power = power
    
    def start_engine(self):
        return f"Engine with {self.power}hp started"

class Radio:
    def __init__(self, brand):
        self.brand = brand
    
    def play_music(self):
        return f"{self.brand} radio is playing music"

# Multiple inheritance
class SportsCar(Vehicle, Engine):
    def __init__(self, make, model, year, power):
        Vehicle.__init__(self, make, model, year)
        Engine.__init__(self, power)
    
    def sport_mode(self):
        return f"{self.make} {self.model} entered sport mode with {self.power}hp!"

class LuxuryCar(Vehicle, Radio):
    def __init__(self, make, model, year, radio_brand):
        Vehicle.__init__(self, make, model, year)
        Radio.__init__(self, radio_brand)
    
    def activate_comfort_mode(self):
        return f"{self.make} {self.model} is in comfort mode with {self.brand} entertainment"

# Testing multiple inheritance
sports_car = SportsCar("Ferrari", "F8", 2023, 710)
luxury_car = LuxuryCar("Mercedes", "S-Class", 2022, "Burmester")

print(sports_car.start())  # From Vehicle
print(sports_car.start_engine())  # From Engine
print(sports_car.sport_mode())  # From SportsCar

print(luxury_car.start())  # From Vehicle
print(luxury_car.play_music())  # From Radio
print(luxury_car.activate_comfort_mode())  # From LuxuryCar
print()

# 7. Class and Static Methods
print("7. Class and Static Methods")
print("-" * 50)

class MathOperations:
    # Class variable
    pi = 3.14159
    
    def __init__(self, value):
        self.value = value
    
    # Instance method - operates on instance
    def double(self):
        return self.value * 2
    
    # Class method - operates on class
    @classmethod
    def from_string(cls, value_str):
        value = float(value_str)
        return cls(value)
    
    @classmethod
    def get_pi(cls):
        return cls.pi
    
    # Static method - doesn't operate on instance or class
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def is_positive(num):
        return num > 0

# Using class and static methods
math_obj = MathOperations(5)
print(f"Instance method: {math_obj.double()}")

# Class method to create new instance
math_obj2 = MathOperations.from_string("10.5")
print(f"Object created from string: {math_obj2.value}")
print(f"Pi from class method: {MathOperations.get_pi()}")

# Static methods
print(f"Addition using static method: {MathOperations.add(3, 7)}")
print(f"Is positive check: {MathOperations.is_positive(-5)}")
print()

# 8. Advanced Features: Properties, Descriptors and Mixins
print("8. Advanced Features: Properties, Descriptors and Mixins")
print("-" * 50)

# Property Example (already covered with BankAccount balance)

# Descriptor Example
class Validation:
    def __init__(self, name=None):
        self.name = name
        self.private_name = f"__{name}"
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)
    
    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) < 2:
            raise ValueError(f"{self.name} must be a string with at least 2 characters")
        setattr(instance, self.private_name, value)

class Person:
    first_name = Validation("first_name")
    last_name = Validation("last_name")
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# Mixin Example
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")
    
    def error(self, message):
        print(f"[ERROR] {message}")

class AdminPermissionMixin:
    admin_permissions = ["read", "write", "delete"]
    
    def has_permission(self, permission):
        return permission in self.admin_permissions

class AdminUser(LoggerMixin, AdminPermissionMixin):
    def __init__(self, username):
        self.username = username
    
    def delete_item(self, item):
        if self.has_permission("delete"):
            self.log(f"User {self.username} deleted {item}")
            return True
        else:
            self.error(f"User {self.username} doesn't have permission to delete")
            return False

# Testing descriptors and mixins
try:
    person = Person("John", "Doe")
    print(f"Full name: {person.full_name}")
    
    # This will raise a ValueError
    person.first_name = "A"
except ValueError as e:
    print(f"Validation error: {e}")

# Testing mixins
admin = AdminUser("admin1")
print(admin.delete_item("file.txt"))
print(f"Admin has write permission: {admin.has_permission('write')}")
