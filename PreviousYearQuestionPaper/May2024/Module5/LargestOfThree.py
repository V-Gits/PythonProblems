#Question
"""
Write a python program to find out the eldest and youngest of three individuals ,
with their ages being input through the keyboard.(without using max, min
functions)
"""
#Approach
"""
Check if the First person age is greater than other three if yes he is set to be eldest and
remaning two are compared for the Youngest
These two steps are done with remaing two persons
"""

NAMES = input("Enter the NAME of three individuals (Seperated by Commas): ").split(",")
AGE = list(map(int, input("Enter the AGE of  three individuals in the order with Name Entered (Seperated by Commas): ").split(",")))

if AGE[0] > AGE[1] and AGE[0] > AGE[2]:
    Eldest = NAMES[0]
elif AGE[1] > AGE[0] and AGE[1] > AGE[2]:
    Eldest = NAMES[1]
elif AGE[2] > AGE[0] and AGE[2] > AGE[1]:
    Eldest = NAMES[2]

if AGE[0] < AGE[1] and AGE[0] < AGE[2]:
    Youngest = NAMES[0]
elif AGE[1] < AGE[0] and AGE[1] < AGE[2]:
    Youngest = NAMES[1]
elif AGE[2] < AGE[0] and AGE[2] < AGE[1]:
    Youngest = NAMES[2]

print(f"""
        Eldest of all these individuals is : {Eldest}
        Youngest of all these individul is: {Youngest}
""")