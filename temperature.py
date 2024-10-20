class Temperature:
    def convertFahrenheit(self, celsius):
        # Converting Celsius to Fahrenheit
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    def convertCelsius(self, fahrenheit):
        # Converting Fahrenheit to Celsius
        celsius = (fahrenheit - 32) * 5/9
        return celsius

#Example
t = Temperature()

# Converting 37°C to Fahrenheit
print(t.convertFahrenheit(37))  

# Converting 40°F to Celsius
print(t.convertCelsius(40)) 
