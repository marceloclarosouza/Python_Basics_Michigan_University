#Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
sent_split = sent.split()
print(sent_split)
strings = []
acro = ""

for i in sent_split:
    if not i in stopwords:
        strings.append(i[0:2])

print(strings)
acro = '. '.join([str(i) for i in strings])
acro = acro.upper()

print(acro)




