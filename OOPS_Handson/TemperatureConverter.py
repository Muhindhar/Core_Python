class TemperatureConverter:
    @staticmethod
    def celsiusToFahrenheit(c):
        return c*9/5+32
    @staticmethod
    def fahrenheitToCelsius(f):
        return (f-32)*5/9

c = float(input("Enter celsius : "))
f = float(input("Enter fahrenheit : "))
print("Fahrenheit :",TemperatureConverter.celsiusToFahrenheit(c))
print("Celsius :",TemperatureConverter.fahrenheitToCelsius(f))
