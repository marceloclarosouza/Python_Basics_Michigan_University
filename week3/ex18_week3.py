#Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num = 0
for i in items:
    if 'w' in i:
        acc_num += 1

print(acc_num)