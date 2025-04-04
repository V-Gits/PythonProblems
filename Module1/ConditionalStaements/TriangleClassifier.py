def rightTriangleChecker(base, perpendicular, hypotenuse):
    if base > 0 and perpendicular > 0 and hypotenuse > 0:
        if (base**2) + (perpendicular**2) == (hypotenuse**2):
            return True
        else:
            return False



SideA = int(input("Enter the Side A: "))
SideB = int(input("Enter the Side B: "))
SideC = int(input("Enter the Side C: "))

if SideA == SideB == SideC:
    print("Equilateral Triangle")
elif SideA == SideB or SideA == SideC or SideB == SideC:
    print("Isosceles Triangle")
else:
    if rightTriangleChecker(SideA, SideB, SideC) or rightTriangleChecker(SideA, SideC, SideB) or rightTriangleChecker(SideB, SideC, SideA):
        print("Right Triangle")
    else:
        print("Scalene Triangle")