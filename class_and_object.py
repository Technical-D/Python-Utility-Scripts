class Circle(object):

    def __init__(self, color, radius):
        self.radius = radius
        self.color = color

    def add_radius(self, r):

        self.radius +=r

        return self.radius
        

c1 = Circle('Red', 5)
c1.color = 'Blue'
c1.radius = 10
c1.add_radius(5)

print(c1.radius)

# Another example
class Car:
    # Class attribute (shared by all instances)
    max_speed = 120  # Maximum speed in km/h
    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0
    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed

    def deaccelerate(self, deacceleration):
        if self.speed == 0 or self.speed < deacceleration:
            self.speed = 0
        else:
            self.speed -= deacceleration


    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed
    
# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

car1.accelerate(150)
car2.accelerate(200)
print(car1.speed)

# Print the current speeds of the cars
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")

car1.deaccelerate(50)
car2.deaccelerate(60)

print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")