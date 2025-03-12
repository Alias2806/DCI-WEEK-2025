# EASY PROBLEM
from math import factorial

#imported factorial function from python math library
#accept user input and store into num, also typecast into int
num = int(input("Input: "))
#print the output with the factorial function of num
print("Output: " + str(factorial(num)))

#AVERAGE PROBLEM
#accept user input and store into input_string
input_string = input("Enter a string: ")
#create empty map
map = {}

#loop through input_string and add into map the character as a key to the map, with the values as the count
for i in range(len(input_string)):
    count = 1
    if(map.__contains__(input_string[i])):
        count += 1
    map[input_string[i]] = count

#create result string
result = ""
#loop through input string and check if the character has a value equal to 1, meaning it is unique
for i in range(len(input_string)):
    if(map.__contains__(input_string[i]) and map.get(input_string[i]) == 1):
        result += input_string[i] + " "
#print out the result
print(result)


