#Implement the calculator for the date of Easter. The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.

year = int(input("type a year between 1900 and 2099 "))
if year < 1900 or year > 2099:
    print("Invalid period!")
    year = int(input("type a year between 1900 and 2099 "))

a = year % 19
b = year % 4
c = year % 7
d = (19*a +24) % 30
e = (2*b + 4*c +6*d +5) % 7
dateofeaster = 22 + d + e
if year == 1954 or year == 1981 or year == 2049 or year == 2076:
    dateofeaster = dateofeaster -7
    dateofeaster = dateofeaster -31
    print("April", dateofeaster)
else:
    dateofeaster = dateofeaster -31
    print("April", dateofeaster)
