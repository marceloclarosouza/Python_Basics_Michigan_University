#Get the user to enter some text and print out True if it’s a palindrome, False otherwise. (Hint: Start by reversing the input string, and then use the == operator to compare two values to see if they are the same)

text = input("Type a sentence ")
text2 = "".join(text.split())#remove the spaces among the strings
text3 = text2[::-1]
print(text)
print(text3)

if text2 == text3:
    print("This is palindrome")
else:
    print("This is not a palidrome")