#Create an empty string and assign it to the variable lett. Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").

lett = []

for i in range(8):
    lett = ("b"*i)

print(lett)