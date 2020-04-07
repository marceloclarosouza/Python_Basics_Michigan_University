#Provided is a list of numbers. For each of the numbers in the list, determine whether they are even. If the number is even, add True to a new list called is_even. If the number is odd, then add False.

num_lst = [3, 20, -1, 9, 10]
is_even = []
for i in num_lst:
    if i % 2 == 0:
        is_even.append(True)
    else:
        is_even.append(False)

print(is_even)