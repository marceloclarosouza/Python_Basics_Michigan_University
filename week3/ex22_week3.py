#We have written conditionals for you to use. Create the variable x and assign it some integer so that at the end of the code, output will be assigned the string "Consistently working".

x = int(input("Type a number "))

if x >= 10:
    output = "working"
else:
    output = "Still working"
if x > 12:
    output = "Always working"
elif x < 7:
    output = "Forever working"
else:
    output = "Consistently working"

print(output)