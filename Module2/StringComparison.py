STRING1 = "APPLE"
string1 = "apple"
STRING2 = "BANANA"
if string1 == STRING1:
    print("Strings are Equal")
elif string1 != STRING1:
    print("Strings are not equal")

if STRING1>STRING2:
    print(f"{STRING1} comes after {STRING2}")
elif STRING1<STRING2:
    print(f"{STRING1} comes before {STRING2}")

if STRING1>string1:
    print(f"{STRING1} comes adfter {string1}")
elif STRING1<string1:
    print(f"{STRING1} comes before {string1}")

#Output
"""
Strings are not equal
APPLE comes before BANANA
APPLE comes before apple
"""