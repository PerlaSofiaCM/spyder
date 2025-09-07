"""
Program: lightyear.py

This program calculates the light years in meters.
"""
#input variables
years = int(input("Enter the number of years: "))

#calculating variables
lightSpeed = 9.46 * (10 ** 12)
lightYears = lightSpeed * years

#display variable
print("Light travels", int(lightYears), "meters in", years, "years.")
