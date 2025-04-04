YEAR = int(input("Enter the Year: "))
if YEAR%4 == 0:
    if YEAR%100 == 0:
        if YEAR%400 == 0:
            print(f"The year {YEAR} IS a Leap Year")
        else:
            print(f"The year {YEAR} IS NOT a Leap Year")
    else:
        print(f"The year {YEAR} IS a Leap year")
else:
    print(f"The year {YEAR} IS NOT a Leap year")
