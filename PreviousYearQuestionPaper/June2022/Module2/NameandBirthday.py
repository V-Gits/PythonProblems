"""
Create a dictionary of names and birthdays. Write a Python program that asks
the user to enter a name, and the program display the birthday of that person.
"""

INFO = {
    "John": "1990-01-01",
    "Alice": "1995-02-02",
    "Bob": "1992-03-03",
}

name = input("Enter the name: ").capitalize()
if name in INFO:
    print(f"{name}'s birthday is {INFO[name]}")