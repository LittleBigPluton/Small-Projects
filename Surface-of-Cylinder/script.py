#!/usr/bin/python3
##############################
####   Import libraries   ####
##############################

import math

##############################
####     Cylinder Area    ####
##############################

class Circle:

    # Initialize the class and radius
    def __init__(self,radius):
        self.radius = radius
    # Setting function for redius
    def set_radius(self,radius):
        self.radius = radius
    # To get radius to out of the class if needed
    def get_radius(self):
        return self.radius
    # To calculate area with the given radius
    def get_area(self):
        return math.pi*self.radius**2
    # To calculate perimeter with the given radius
    def get_perimeter(self):
        return 2*math.pi*self.radius

class Cylinder(Circle):

    def __init__(self,radius,height):
        super().__init__(radius)
        self.height = height

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.get_area()*self.height

    def get_surface(self):
        return 2*self.get_area()+self.get_perimeter()*self.height

Circ = Circle(int(input("Enter radius: ")))
Radius = Circ.get_radius()
Area = Circ.get_area()
PM = Circ.get_perimeter()

print(f'Circle with radius {Radius}')
print(f'Area of the Circle is {Area}')
print(f'Perimeter of the circle is {PM}')

height = int(input("Enter height of cylinder: "))
Cyl = Cylinder(Radius,height)
Height = Cyl.get_height()
Volume = Cyl.get_volume()
SA = Cyl.get_surface()

print(f'Cylinder with height {Height} and radius {Radius}')
print(f'Cylinder\'s volume is {Volume}')
print(f'Cylinder\'s surface area is {SA}')
