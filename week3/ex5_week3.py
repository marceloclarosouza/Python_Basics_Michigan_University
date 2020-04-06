#We have created conditionals for you to use. Do not change the provided conditional statements. Find an integer value for x that will cause output to hold the values True and None. (Drawing diagrams or flow charts for yourself may help!)

x = int(input("Type a number"))
output = []

if x > 63:
    output.append(True)
elif x > 55:
    output.append(False)
else:
    output.append("Neither")

if x > 67:
    output.append(True)
else:
    output.append(None)

print(output)