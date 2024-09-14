import math
# program for calculating surface area of cylinder 
radius =float(input("Enter the radius of the cylinder: "))
height =float(input("Enter the height of the cylinder: "))
surface_area=2 *math.pi*radius**2+2*math.pi*radius*height
print(f"Surface area of the cylinder is: {surface_area:.2f}")
