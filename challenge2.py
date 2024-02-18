# K.
# Create a nested for loop (loop inside another loop) to create
# a pyramid shape:

for i in range(5):
    str = "#"
    for x in range(i):
        str = str + "#"
    print(str)

print("--------------------------------------")

# L.
# Create a nested for loop to create X shape (width is 7,
# length is 7):

str = ""
for i in range(7):
    for x in range(7):
        if i == x or i == (6-x):
            str = str + "#"
        else:
            str = str + " "
    print(str)
    str = ""

print("--------------------------------------")

# M.
# Write a program with the following:
# 1. Method that gets a number from the user (using input).
# 2. Method that receive the number from the first method, and
# computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)

def input_numer():
    num = input("Please enter 2+ digit integer: ")
    return (num)

def sum_of_digits(num):
    num1 = (int(num))
    sum = 0
    for i in range(len(num)):
        digit = num1 % 10
        num1 = num1 // 10
        sum = sum + digit
    return (sum)

number = input_numer()
print("sum of digits: ", sum_of_digits(number))

