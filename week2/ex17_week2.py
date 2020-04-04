#week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

data = week_temps_f.split(",")
print(data)

data_int = [float(i) for i in data]
print(data_int)

cont = 0
for i in data_int:
    cont += i

print(cont)
avg_temp = cont/(len(data_int))
print(avg_temp)
