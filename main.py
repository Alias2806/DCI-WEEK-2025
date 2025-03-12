
# EASY PROBLEM
from math import factorial
print ("EASY PROBLEM")
#imported factorial function from python math library
#accept user input and store into num, also typecast into int
num = int(input("Input: "))
#print the output with the factorial function of num
print("Output: " + str(factorial(num)))

print("\nEASY PROBLEM alt solution")
#accept user input
num2 = int(input("Input: "))
temp_num = num2
#set default value for res as 1 since 0! is 1
res = 1
for i in range(num2):
    #multiply num2 and decrement and store into res
    res *= temp_num
    temp_num -= 1
#print output
print("Output: " + str(res))

#AVERAGE PROBLEM
print ("\nAVERAGE PROBLEM")
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

# HARD PROBLEM
print("\nHARD PROBLEM")
#user input the number of items purchased(number of loops to be done)
num_of_items_purchased = int(input("Enter the number of items purchased: "))
#to find out if customer has VIP discount
customer_type = input("Enter customer type (Regular/VIP): ")

#for receipt generation
total_price: float = 0
item_totals = []
item_prices = []
item_quantities = []
item_names = []

#where user inputs the product details
def selectProduct():
    item_name = input("Item name: ")
    item_price = float(input("Item price: "))
    item_quantity = float(input("Item quantity: "))
    item_names.append(item_name)
    item_prices.append(item_price)
    item_quantities.append(item_quantity)
    item_totals.append(item_quantity * item_price)
    return item_price * item_quantity

#main loop that depends on num of items purchased
for i in range(1, num_of_items_purchased + 1):
    print("Enter details for item " + str(i))
    total_price += selectProduct()

subtotal = total_price

#discount application
vip_discount: float = 0
if customer_type.lower() == "vip":
    vip_discount = total_price * 0.1
    total_price = total_price - (total_price * 0.1)

#tax application
tax: float = 0
if total_price > 500:
    tax = total_price * 0.05
    total_price = total_price + (total_price * 0.05)

#Receipt generation
print("=======Grocery Store Receipt=======")
for i in range(len(item_names)):
    print("Item: " + str(item_names[i]) + "| Qty: " + str(item_quantities[i]) + "| Price: PHP" + str(item_prices[i]) + "| Total: PHP" + str(item_totals[i]))
print("----------------------------------")
print("Subtotal: PHP" + str(subtotal))
print("VIP Discount (10%): -PHP" + str(vip_discount))
print("Tax (5%): +PHP" + str(tax))
print("----------------------------------")
print("Final Total: PHP" + str(total_price))
print("Thank you for shopping with us!")