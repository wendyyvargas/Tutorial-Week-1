import math
# to access math functions and constants like math.pi

# --- Functions ---
def areaRectangle(length, width):
    """
    Calculate and return the area of a rectangle.
    Parameters:
      length (float): length of the rectangle
      width (float): width of the rectangle
    Returns:
      float: area of the rectangle
    """
    # TODO: Implement this function
    pass #delete this once function is written 

def areaTriangle(base, height):
    """
    Calculate and return the area of a triangle.
    Parameters:
      base (float): base length of the triangle
      height (float): height of the triangle
    Returns:
      float: area of the triangle
    """
    # TODO: Implement this function
    pass #delete this once function is written 

def areaCircle(radius):
    """
    Calculate and return the area of a circle.
    Parameters:
      radius (float): radius of the circle
    Returns:
      float: area of the circle
    """
    # TODO: Implement this function
    pass #delete this once function is written 

# --- Main Program ---

print("Welcome to the Shape Area Calculator!")
print("Enter 'R' for Rectangle, 'T' for Triangle, or 'C' for Circle.")

shape = input("Your choice: ").strip().lower()

if shape == "r":
    # TODO: Ask for length and width as floats
    # length = float(input("Enter the length: "))
    # width = float(input("Enter the width: "))
    # TODO: Calculate area using areaRectangle()
    # TODO: Print the result nicely formatted
    pass

elif shape == "t":
    # TODO: Ask for base and height as floats
    # base = float(input("Enter the base: "))
    # height = float(input("Enter the height: "))
    # TODO: Calculate area using areaTriangle()
    # TODO: Print the result nicely formatted
    pass

elif shape == "c":
    # TODO: Ask for radius as a float
    # radius = float(input("Enter the radius: "))
    # TODO: Calculate area using areaCircle()
    # TODO: Print the result nicely formatted
    pass

else:
    print("Invalid shape choice. Please run the program again and choose R, T, or C.")
