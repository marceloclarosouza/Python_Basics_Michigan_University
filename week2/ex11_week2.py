#How many times is the letter p printed by the following statements?

s = "python"
for idx in range(len(s)):
    #print(idx % 2)
    print(s[idx % 2])