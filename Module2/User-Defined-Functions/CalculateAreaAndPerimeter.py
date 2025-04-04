def Calculate_Area_and_perimeter(LENGTH, BREADTH):
    AREA = LENGTH * BREADTH
    PERIMETER = 2*(LENGTH + BREADTH)
    return AREA, PERIMETER

LENGTH = int(input("Enter the Length of rectangle: "))
BREADTH = int(input("Enter the Breadth of rectangle: "))
AREA, PERIMETER = Calculate_Area_and_perimeter(LENGTH, BREADTH)
print(f"{AREA= }")
print(f"{PERIMETER= }")