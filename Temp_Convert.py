# Ask the user for a temperature
temp = input("Enter Temperature: ")

# Convert Celsius to Fahrenheit
def cels_to_fahr(tempc):
    fahr = (9 / 5) * (tempc) + 32
    print(f"It is {round(fahr)} Fahrenheit")

# Convert Fahrenheit to Celsius
def fahr_to_cels(tempf):
    cels = (tempf - 32) * (5 / 9)
    print(f"It is {round(cels)} Celsisus")

# Figure out if Fahrenheit or Celsius
if temp[-1] == "f":
    tempf = float(temp[:-1])
    fahr_to_cels(tempf)
elif temp[-1] == "c":
    tempc = float(temp[:-1])
    cels_to_fahr(tempc)
else:
    print("Please end input with either 'f' or 'c'")
