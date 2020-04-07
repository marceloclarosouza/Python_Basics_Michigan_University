#Given the lengths of three sides of a triange, determine whether the triangle is right angled. If it is, the assign True to the variable is_rightangled. If it’s not, then assign False to the variable is_rightangled.

a = 5
b = 6
c = 8

if (a**2 + b**2) == c**2:
    is_rightangled = True
else:
    is_rightangled = False

print(is_rightangled)