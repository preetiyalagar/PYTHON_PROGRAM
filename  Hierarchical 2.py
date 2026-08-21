#Hierarchial Inheritanc using Python
class Vehicle:
    def show_Vehicle(self):
        print("This is a Vehicle")
class Car(Vehicle):
    def show_Car(self):
        print("This is a Car")
class Bike(Vehicle):
    def show_Bike(self):
        print("This is a Bike")
class Bus(Vehicle):
    def show_Bus(self):
        print("This is a Bus")
c=Car()
b=Bike()
bus=Bus()

c.show_Vehicle()
c.show_Car()

b.show_Vehicle()
b.show_Bike()

bus.show_Vehicle()
bus.show_Bus()
