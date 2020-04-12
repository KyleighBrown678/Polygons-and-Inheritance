#Kyleigh Brown
#You will write a program that creates a base class Polygon with the following details:
import math

#class Polygon
class Polygon:
    def __init__(self, num_of_sides):
        #Parameterized constructor which takes num_of_sides as a parameter
        #attributes:
        #n(integer) refers to the number of sides for the polygon
        self.n = num_of_sides
        
        #sides(list) containing the lengths of each side of the polygon object
        self.sides = []
        self.perimeter = 0.0

    def findPerimeter(self):
        #findPerimeter: takes as input the sides of the polygon and outputs the polygon's perimeter
        for i in range(self.n):
            self.sides.append(float(input("Enter the length of a side: ")))

        for item in self.sides:
            self.perimeter += item
    
    def dispSide(self):
        #dispSide: displays the length for each side
        print('This polygon has %d sides' % len(self.sides))
        print('This polygon has sides with lengths', self.sides)
        print()

    def __str__(self):
        self.dispSide()
        return('The perimeter is %.02f' % self.perimeter)
#3 subclasses:
    #appropriate methods for finding the area and perimeter
    #(?)str method: prints properties of the polygon subclass
        
class Triangle(Polygon):
    def __init__(self, num_of_sides = 3):
        Polygon.__init__(self, num_of_sides)
        self.area = 0.0
    
    def findPerimeter(self):
        Polygon.findPerimeter(self)
        
    def dispSide(self):
        #dispSide: displays the length for each side
        print('This triangle has %d sides' % len(self.sides))
        print('This triangle has sides with lengths', self.sides)
        print()

    def findArea(self):
        self.area = self.sides[0] * self.sides[1] * 0.5
        print('The area of the right triangle is 5.2f' % self.area)
        print()

    def __str__(self):
        Polygon.__str__(self)

        
class Square(Polygon):
    def __init__(self, num_of_sides = 4):
        Polygon.__init__(self, num_of_sides)
        self.area = 0.0

    def findPerimeter(self):
        Polygon.findPerimeter(self)

    def dispSide(self):
        print('This square has %d sides' % len(self.sides))
        print('This square has sides with lengths', self.sides)
        print()

    def findArea(self):
        self.area = self.sides[0]*self.sides[1]
        print('The area of this square is %.2f' % self.area)
        print()

    def __str__(self):
        Polygon.__str__(self)


class Pentagon(Polygon):
    def __init__(self, num_of_sides = 5):
        Polygon.__init__(self, num_of_sides)
        self.area = 0.0

    def findPerimeter(self):
        Polygon.findPerimeter(self)

    def dispSide(self):
        print('This pentagon has %d sides' % len(self.sides))
        print('This pentagon has sides with lengths', self.sides)
        print()

    def findArea(self):
        self.area = ((5 * self.sides[0]) ** 2)/ (4 * math.sqrt(5- 2 * math.sqrt(5)))
        print('The area of this pentagon is %.2f' % self.area)
        print()

    def __str__(self):
        Polygon.__str__(self)

        
def main():
    shape = Polygon(3)
    shape.findPerimeter()
    shape.dispSide()
    print(shape)

    tri = Triangle()
    tri.findPerimeter()
    tri.dispSide()
    tri.findArea()
    print(tri)

    square = Square()
    square.findPerimeter()
    square.dispSide()
    square.findArea()
    print(square)

    pentagon = Pentagon()
    pentagon.findPerimeter()
    pentagon.dispSide()
    pentagon.findArea()
    print(pentagon)
main()
