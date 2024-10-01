class Rectangle:
    def __init__(self, length, width):
        """Initialize the length and width of the rectangle."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

# Example usage:
rect = Rectangle( 5, 3)
print("Area:", rect.area())            
print("Perimeter:", rect.perimeter())



#task 2
class Animal:
    def __init__(self, name):
        """Initialize the animal with a name."""
        self.name = name
    
    def speak(self):
        """Common method to be overridden by derived classes."""
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        """Override the speak method for Dog."""
        return f"{self.name} says Woof!"

    def fetch(self):
        """Unique method for Dog."""
        return f"{self.name} is fetching the ball!"

class Cat(Animal):
    def speak(self):
        """Override the speak method for Cat."""
        return f"{self.name} says Meow!"

    def scratch(self):
        """Unique method for Cat."""
        return f"{self.name} is scratching the furniture!"

class Bird(Animal):
    def speak(self):
        """Override the speak method for Bird."""
        return f"{self.name} says Chirp!"

    def fly(self):
        """Unique method for Bird."""
        return f"{self.name} is flying high!"

# Instantiate objects of each class
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

# Demonstrate polymorphism
animals = [dog, cat, bird]
for animal in animals:
    print(animal.speak())

# Call unique methods
print(dog.fetch())
print(cat.scratch())
print(bird.fly())



import math

class Shape:
    def area(self):
        """Method to be overridden by subclasses to calculate the area."""
        raise NotImplementedError("Subclass must implement the area method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)


rect = Rectangle(5, 3)
circle = Circle(4)

# Print the areas
print("Rectangle Area:", rect.area())  
print("Circle Area:", circle.area())    