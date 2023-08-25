import math

def getCircumference(r):

    circumference = 2 * math.pi * r

    print(f"The circumference of your circle is: {round(circumference, 2)}")

def getArea(r):

    area = math.pi * r * r

    print(f"The area of your circle is: {round(area, 2)}")

def main():
    radius = input("Enter the radius: ")

    getArea(int (radius))
    getCircumference(int (radius))


main()
