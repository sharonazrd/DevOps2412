# A.
# 1. Create two variables name X and Y.
# 2. Print “BIG” if X is bigger than Y .
# 3. Print “small” if X is smaller than Y.

x = 5
y = 6

if x > y:
    print("big")
elif x < y:
    print("small")

print("--------------------------------------")

# B.
# 1. Run a “for” loop 5 times.
# 2. Print iteration number every time.

for i in range(5):
    print(i)

print("--------------------------------------")

# C.
# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable.
# 3. print the season name accordingly:
#
# - 1 = summer
# - 2 = winter
# - 3 = fall
# - 4 = spring

season = 5
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")
else:
    print("wrong number")

print("--------------------------------------")

# D.
# 1. how many times will the following loop run? 11
# 2. what will be printed last? 10

count = 1
while count < 11:
    print(count)
    count = count + 1

print("--------------------------------------")

# E.
# Write a program with variables holding the following:
# 1. Your age.
# 2. First letter of your last name.
# 3. Current shekels-dollar currency.
# 4. Did you flew abroad (true/false)
# 5. Your apartment number.
#
# ● Print all variables.
# ● Add the currency to your age, and check the result.

my_age = 50
first_letter_last_name = "a"
shekel_dollar = 3.6
flew_aboard = "false"
apartment_number = 39

print("my_age: ", my_age, "\nfirst letter of my last name: ", first_letter_last_name, "\ncurrent shekels-dollar currency: ", shekel_dollar, "\nDid you flew abroad?", flew_aboard, "\nmy apartment number:", apartment_number)
print(my_age + shekel_dollar)

print("--------------------------------------")

# F.
#
# Create a program which uses input with the following:
# 1. Ask user for his phone number
# 2. Print the words “phone number” and the phone number the
# user entered.

phone_number = input("please enter your phone number: ")
print("phone number:", phone_number)

print("--------------------------------------")

# G.
#
# Write a program with the following:
# 1. Method named printHello() that prints the word “hello”.
# 2. Method named calculate() which adds 5+3.2 and prints the
# result.

def printHello():
    print("hello")

def calculate():
    print( 5 + 3.2)

printHello()
calculate()

print("--------------------------------------")

# H.
# Write a program with the following:
# 1. Method that receive your name and prints it.
# 2. Method that receive a number, divide it by 2, and prints the
# result.

def print_name():
    name = input("please enter your name: ")
    print(name)

def divid_by_2():
    num1 = input("enter your number: ")
    num2 = int(num1) / 2
    print(num2)

print_name()
divid_by_2()

print("--------------------------------------")

# I.
# Write a program with the following:
# 1. Method that receive two numbers, add them, and return the
# sum.
# 2. Method that receive two Strings, add space between them,
# and return one spaced string.

def add_numbers(num1, num2):
    return num1 + num2

def concat(str1, str2):
    return (str1 + " " + str2)

print(add_numbers(1,2))
print(concat("sha", "ron"))



