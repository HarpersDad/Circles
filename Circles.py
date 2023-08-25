import math

def isItASphere(r):

    volume = (4 / 3) * math.pi * r * r * r
    surfaceArea = 4 * math.pi * r * r

    print(f"\nIf this is a sphere, it's volume is approximately {round(volume, 2)},")
    print(f"and it's surface area is approximately {round(surfaceArea, 2)}")

def getCircumference(r):

    circumference = 2 * math.pi * r

    print(f"The circumference of your circle is: {round(circumference, 2)}")

def getArea(r):

    area = math.pi * r * r

    print(f"\nThe area of your circle is: {round(area, 2)}")

def main():
    radius = input("Enter the radius: ")

    getArea(int(radius))
    getCircumference(int(radius))
    isItASphere(int(radius))


main()
