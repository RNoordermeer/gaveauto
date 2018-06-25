
import random


class Car:
    color = "red"
    max_speed = 300 # in km/h
    velocity = 0 # in km/h
    traveltime = 0 # in seconds

    def __init__(self):
        self.color = random.choice(["green", "yellow", "white", "blue"])
        self.heading = random.randint(0, 360)
        self.max_speed = random.randint(0, 400)
        self.velocity = random.randint(0, self.max_speed)
        self.traveltime = random.randint(0, 1000)

    def traveled_distance(self):
        """calculates the distance this car traveled given the time and velocity"""
        result = self.velocity * (self.traveltime / 3600) # in km
        return result

    def print_properties(self):
        print (self.color + ", " + str(self.velocity) + "km/h, " + str(self.heading) + "deg, "
               + str(self.traveled_distance()) + "km")

car1 = Car()
car2 = Car()

car1.print_properties()
car2.print_properties()

