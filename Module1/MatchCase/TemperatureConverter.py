def CelsiusToKelvin(temp):
    return temp + 273.15

def KelvinToCelsius(temp):
    return temp - 273.15

def CelsiusToFahrenheit(temp):
    return (temp * (9/5)) + 32

def FahrenheitToCelsius(temp):
    return (temp - 32) * (5/9)

def FahrenheitToKelvin(temp):
    return (temp - 32) * 5/9 + 273.15

def KelvinToFahrenheit(temp):
    return (temp - 273.15) * 9/5 + 32


ch = int(input("""
        Temperature Converter
      1.Celsius To Kelvin
      2.Kelvin To Celsius
      3.Celsius To Fahrenheit
      4.Fahrenheit To Celsius
      5.Fahrenheit To Kelvin
      6.Kelvin To Fahrenheit
      Choose the Number Corresponding to the Conversion You Want to Perform
    
Enter the Choice: """))

temp = float(input("Enter the Temperature: "))

match ch:
    case 1:
        new_temp = CelsiusToKelvin(temp)
        print(f"{temp}°C = {new_temp}°K")
    case 2:
        new_temp = KelvinToCelsius(temp)
        print(f"{temp}°K = {new_temp}°C")
    case 3:
        new_temp = CelsiusToFahrenheit(temp)
        print(f"{temp}°C = {new_temp}°F")
    case 4:
        new_temp = FahrenheitToCelsius(temp)
        print(f"{temp}°F = {new_temp}°C")
    case 5:
        new_temp = KelvinToFahrenheit(temp)
        print(f"{temp}°K = {new_temp}°F")
    case 6:
        new_temp = FahrenheitToKelvin(temp)
        print(f"{temp}°F = {new_temp}°K")
    case default:
        print("Invalid Choice")
        