def Celsius_To_Fahreheit(celsius):
    fahrenheit = (celsius *(9/5))+32
    return fahrenheit

celsius = float(input("Enter the temperature is Celsius: "))
fahrenheit = Celsius_To_Fahreheit(celsius)
print(f"{celsius:.2f}C = {fahrenheit:.2f}F")