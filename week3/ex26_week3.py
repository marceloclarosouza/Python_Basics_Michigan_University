#For each string in wrd_lst, find the number of characters in the string. If the number of characters is less than 6, add 1 to accum so that in the end, accum will contain an integer representing the total number of words in the list that have fewer than 6 characters.

wrd_lst = ["Hello", "activecode", "Java", "C#", "Python", "HTML and CSS", "Javascript", "Swift", "php"]
accum = 0
for i in wrd_lst:
    if len(i) < 6:
        accum += 1
print(accum)