#Write code that asks the user to enter a numeric score (0-100). In response, it should print out the score and corresponding letter grade, according to the table below.

x = int(input("Type a number between 0 and 100"))

if x >= 90:
    grade = 'A'
elif x >= 80 and x < 90:
    grade = 'B'
elif x >= 70 and x < 80:
    grade = 'C'
elif x >= 60 and x < 70:
    grade = 'D'
else:
    grade = 'F'

print(grade)