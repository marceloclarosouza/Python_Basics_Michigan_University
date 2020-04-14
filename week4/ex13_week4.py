#In XYZ University, upper level math classes are numbered 300 and up. Upper level English classes are numbered 200 and up. Upper level Psychology classes are 400 and up. Create two lists, upper and lower. Assign each course in classes to the correct list, upper or lower. HINT: remember, you can convert some strings to different types!
classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
upper = []
lower = []
temp = []

for i in classes:
    temp = i.split()
    temp[1] = int(temp[1])
    if temp[0] =="MATH":
        if temp[1] >= 300:
            upper.append(i)
        else:
            lower.append(i)
    elif temp[0] == "PSYCH":
        if temp[1] >= 400:
            upper.append(i)
        else:
            lower.append(i)
    elif temp[0] == "ENG":
        if temp[1] >= 200:
            upper.append(i)
        else:
            lower.append(i)

print(upper)
print(lower)
