from rectangle import Rectangle, Square, Circle

r1 = Rectangle(10, 5)
r2 = Rectangle(100, 7)

# print("r1.width=", r1.width)
# print("r1.height=", r1.height)
# print("r1.getWidth=", r1.getWidth())
print("r1.getArea=", r1.getArea())

# print("r2.width=", r2.width)
# print("r2.height=", r2.height)
# print("r2.getWidth=", r2.getWidth())
print("r2.getArea=", r2.getArea())

s1 = Square(15)
s2 = Square(10)
print(f's1.getSquare = {s1.getSquare()}, s2.getSquare = {s2.getSquare()}')

area_circle1 = Circle(1)
area_circle2 = Circle(2)
print('Area circle 1 = ', area_circle1.getAreaCircle())
print('Area circle 2 = ', area_circle2.getAreaCircle())

figures = [r1, r2, s1, s2, area_circle1, area_circle2]
for figure in figures:
    if isinstance(figure, Square):
        print(f'Area Square =', figure.getSquare())
    elif isinstance(figure, Rectangle):
        print(f'Area Rectangle =', figure.getArea())
    else:
        print(f'Area Circle =', figure.getAreaCircle())

