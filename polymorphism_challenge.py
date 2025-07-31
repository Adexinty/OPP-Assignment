# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves.")

# Subclasses with different move()  implementations
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Create instances
car = Car()
plane = Plane()
boat = Boat()

# Call move() method on each
car.move()
plane.move()
boat.move()
