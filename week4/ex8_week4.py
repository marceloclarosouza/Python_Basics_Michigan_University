#Challenge Now do the same as in the previous problem, but do not create a new list. Overwrite the list numbs so that each of the original numbers are increased by 5.
numbs = [5, 10, 15, 20, 25]
w = 0
for i in numbs:
    numbs[w] = i+5
    w +=1
print(numbs)