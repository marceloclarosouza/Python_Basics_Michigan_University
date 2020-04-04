#addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).

addition_str = "2+5+10+20"

addition_split = addition_str.split("+")
print(addition_split)

result = [int(i) for i in addition_split]#convert the string list on an integer list
print(result)

count = 0
for i in result:
    count += i

sum_val = count
print(sum_val)