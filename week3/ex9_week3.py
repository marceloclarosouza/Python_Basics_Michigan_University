#A year is a leap year if it is divisible by 4. If the year can be evenly divided by 100, it is NOT a leap year, unless the year is also evenly divisible by 400. Then it is a leap year. Write code that asks the user to input a year and output True if it’s a leap year, or False otherwise. Use if statements.

year = int(input("Type a year "))

if year % 4 == 0 and year % 100 != 0:
    leap = True
elif year % 100 == 0 and year % 400 == 0:
    leap = True
else:
    leap = False

print(year, "Is a leap year? ", leap)