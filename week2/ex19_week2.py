#Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).

original_str = "The quick brown rhino jumped over the extremely lazy fox"

word = original_str.split(" ")
print(word)

num_words_list = []#empty list
for i in word:
    num_words_list.append(len(i))#adding the length of each word to the list

print(num_words_list)