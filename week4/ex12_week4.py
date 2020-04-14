#For each word in the list verbs, add an -ing ending. Overwrite the old list so that verbs has the same words with ing at the end of each one
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]

for i in range(len(verbs)):
    verbs[i] = verbs[i]+"ing"

print(verbs)