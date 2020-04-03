# Write a program that will print out the length of each item in the list as well as the first and last characters of the item
weather = ["sunny", "cloudy", "partially sunny", "rainy", "storming", "windy", "foggy", "snowy", "hailing"]

for condition in weather:
    print("the word is ", len(condition), "characters")
    first_char = condition[0]
    last_char = condition[-1]
    print("The first character is: " + first_char)
    print("The last character is: " + last_char)