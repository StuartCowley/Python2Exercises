#  This program is for calculating the area of a given shape inputted by the user
print("The calculator is running")
name = input("Enter C for Circle or T for Triangle: ")
option = name
if option in "Cc":
    radius = float(input("Input radius: "))
    area = radius**2 * 3.141592
    print("Area of circle is %.2f " % area)
elif option in "Tt":
    base = float(input("Input base length: "))
    height = float(input("Input height: "))
    area = base * height * 0.5
    print("Area of triangle is %.2f " % area)
else:
    print("You have entered an invalid value")
print("Program is exiting")
