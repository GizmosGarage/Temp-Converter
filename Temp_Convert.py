# Ask the user for an input
temp = float(input("Enter Fahrenheit: "))

# Convert Fahrenheit to Celsius
def fahr_to_cels(temp):
    cels = (temp - 32) * (5/9)
    return round(cels)

print(fahr_to_cels(temp))
