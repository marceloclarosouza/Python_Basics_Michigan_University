#Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores2 = scores.split()
scores_int = [int(i) for i in scores2]
print(scores_int)


a_scores = 0

for i in range(len(scores_int)):
    if scores_int[i] >= 90:
        a_scores += 1

print(a_scores)