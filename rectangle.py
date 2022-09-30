﻿class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getArea(self):
        return self.width * self.height

class Square:
    def __init__(self, side):
        self.side = side

    def getSquare(self):
        return self.side**2

class Circle:
    def __init__(self, radius, pi=3.14):
        self.radius = radius
        self.pi = pi

    def getAreaCircle(self):
        return self.pi * self.radius**2