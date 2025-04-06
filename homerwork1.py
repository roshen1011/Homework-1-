import math

def circle_area_perimeter():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print(f"The Area of the circle with radius {radius} is {area:.2f} and perimeter is {circumference:.2f}")

circle_area_perimeter()

# cube.py
import math

def cube_area_perimeter():
    side = float(input("Enter the side length of the cube: "))
    surface_area = 6 * side ** 2
    total_edge_length = 12 * side
    print(f"The Surface Area of the cube with side {side} is {surface_area:.2f} and Total Edge Length is {total_edge_length:.2f}")

cube_area_perimeter()

# cylinder.py
import math

def cylinder_area_perimeter():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    surface_area = 2 * math.pi * radius * (radius + height)
    perimeter = 2 * math.pi * radius + 2 * height
    print(f"The Surface Area of the cylinder is {surface_area:.2f} and perimeter is {perimeter:.2f}")

cylinder_area_perimeter()

# sphere.py
import math

def sphere_area_perimeter():
    radius = float(input("Enter the radius of the sphere: "))
    surface_area = 4 * math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print(f"The Surface Area of the sphere is {surface_area:.2f} and the circumference is {circumference:.2f}")

sphere_area_perimeter()

# trapezoid.py
import math

def trapezoid_area_perimeter():
    base1 = float(input("Enter the first base of the trapezoid: "))
    base2 = float(input("Enter the second base of the trapezoid: "))
    side1 = float(input("Enter the first side of the trapezoid: "))
    side2 = float(input("Enter the second side of the trapezoid: "))
    height = float(input("Enter the height of the trapezoid: "))
    area = 0.5 * (base1 + base2) * height
    perimeter = base1 + base2 + side1 + side2
    print(f"The Area of the trapezoid is {area:.2f} and perimeter is {perimeter:.2f}")

trapezoid_area_perimeter()

# pentagon.py
import math

def pentagon_area_perimeter():
    side = float(input("Enter the side length of the pentagon: "))
    area = (5 * side ** 2) / (4 * math.tan(math.pi / 5))
    perimeter = 5 * side
    print(f"The Area of the pentagon is {area:.2f} and perimeter is {perimeter:.2f}")

pentagon_area_perimeter()

# hexagon.py
import math

def hexagon_area_perimeter():
    side = float(input("Enter the side length of the hexagon: "))
    area = (3 * math.sqrt(3) * side ** 2) / 2
    perimeter = 6 * side
    print(f"The Area of the hexagon is {area:.2f} and perimeter is {perimeter:.2f}")

hexagon_area_perimeter()

