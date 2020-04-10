#For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing=[]
for i in verbs:
    i += 'ing'
    ing.append(i)
print(ing)
