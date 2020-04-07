#Provided are the lengths of two sides of a right-angled triangle. Assign the length of the hypotenuse the the variable hypo_len. (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)

import math

a = 3
b = 4
hypo_len = math.sqrt((a**2) + (b**2))
print(hypo_len)