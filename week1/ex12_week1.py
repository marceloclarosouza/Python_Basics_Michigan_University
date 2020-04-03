#Ask the user for the temperature in Fahrenheit and store it in a variable call deg_f. Calculate the equivalent temperature in degrees Celsius and store it in def_c. Output a message to the user giving the temperature in Celsius.

deg_f = float(input("Digite a temp em Fahrenheit"))
deg_c = (deg_f -32)*(5/9)
print(deg_c)