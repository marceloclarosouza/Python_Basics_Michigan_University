#Provided is a list of numbers. For each of the numbers in the list, determine whether they are odd. If the number is odd, add True to a new list called is_odd. If the number is even, then add False.
num_lst = [3, 20, -1, 9, 10]
is_odd = []

for i in num_lst:
    if i % 2 != 0:
        is_odd.append(True)
    else:
        is_odd.append(False)

print(is_odd)