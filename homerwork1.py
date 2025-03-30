import math

def calculate_shape(shape):
    if shape == "circle":
        r = float(input("Enter radius: "))
        area, perimeter = math.pi * r**2, 2 * math.pi * r
    elif shape == "cube":
        s = float(input("Enter side length: "))
        area, perimeter = 6 * s**2, 12 * s
    elif shape == "cylinder":
        r, h = float(input("Enter radius: ")), float(input("Enter height: "))
        area, perimeter = 2 * math.pi * r * (r + h), 2 * math.pi * r + 2 * h
    elif shape == "sphere":
        r = float(input("Enter radius: "))
        area, perimeter = 4 * math.pi * r**2, 2 * math.pi * r
    elif shape == "trapezoid":
        b1, b2, h, s1, s2 = (float(input(f"Enter {x}: ")) for x in ["base 1", "base 2", "height", "side 1", "side 2"])
        area, perimeter = 0.5 * (b1 + b2) * h, b1 + b2 + s1 + s2
    elif shape == "pentagon":
        s = float(input("Enter side length: "))
        area, perimeter = (5 * s**2) / (4 * math.tan(math.pi / 5)), 5 * s
    elif shape == "hexagon":
        s = float(input("Enter side length: "))
        area, perimeter = ((3 * math.sqrt(3)) / 2) * s**2, 6 * s
    else:
        print("Invalid shape!")
        return