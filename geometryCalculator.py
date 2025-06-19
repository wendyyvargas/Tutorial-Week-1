import math
# to access math functions and constants like math.pi

# --- Functions ---

# Calculate and return the area of a rectangle.
def areaRectangle(length, width):
    area = length * width
    return area

 # Calculate and return the area of a triangle.
def areaTriangle(base, height):
    area = base * height * 0.5
    return area

 # Calculate and return the area of a circle.
def areaCircle(radius):
    area = math.pi * radius * radius
    return area

# --- Main Program ---

print("Welcome to the Shape Area Calculator!")
print("Enter 'R' for Rectangle, 'T' for Triangle, or 'C' for Circle.")

shape = input("Your choice: ").strip().lower()

# these are called conditionals, there will be more information about them next week
# they are meant to check if a condition is true, if so, it runs
# for now, just use this template we gave you :)
if shape == "r":
    #Ask for length and width as floats
    length = float(input("Please enter the length of the rectangle: "))
    width = float(input("Please enter the width of the rectangle: "))
    #Calculate area using areaRectangle()
    area = areaRectangle(length,width)
    #Print the result nicely formatted
    print("The area of your rectangle is: " + str(area))  #1.0 but now "1.0"

elif shape == "t":
    # Ask for base and height as floats
    base = float(input("Please enter the base of the triangle: "))
    height = float(input("Please enter the height of the triangle: "))
    # Calculate area using areaTriangle()
    area = areaTriangle(base, height)
    # Print the result nicely formatted
    print("The area of your triangle is: " + str(area))

elif shape == "c":
    # Ask for radius as a float
    radius = float(input("Enter the radius: "))
    #Calculate area using areaCircle()
    area = areaCircle(radius)
    # Print the result nicely formatted
    print("The area of your circle is: " + str(area))

else:
    print("Invalid shape choice. Please run the program again and choose R, T, or C.")
