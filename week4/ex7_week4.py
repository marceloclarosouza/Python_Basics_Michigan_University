#Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist.
numbs = [5, 10, 15, 20, 25]
newlist=[]
for i in numbs:
    i +=5
    newlist.append(i)
print(newlist)