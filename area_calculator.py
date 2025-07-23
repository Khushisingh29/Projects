import math
print("Welcome to area calculator")
print("Select the shape")
print("1) Circle")
print("2) Triangle")
print("3) Square")
print("4) Rectangle")

Select=int(input("Enter the shape between(1-4): "))
if Select==1:
    radius=int(input("Enter the radius: "))
    area=math.pi*radius**2
    print("the area of circle: ", area)

elif Select==2:
    base=int(input("Enter the base= "))
    height=int(input("Enter the height: "))
    area = 1/2*base*height
    print("the area of Triangle: ", area)

elif Select==3:
     side1=int(input("Enter the side1= "))
     side2=int(input("Enter the side2= "))
     area= side1*side2
     print("the area of Square: ", area)

elif Select==4:
    length=int(input("Enter the length of rectangle= "))
    width=int(input("Enter the width of rectangle= "))
    area= length*width
    print("the area of rectangle: ", area)     

else:
    print("Invalid Input")    