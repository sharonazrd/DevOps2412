a = 50
b = 10
my_name = "sharon"
if a < 10 and b >5:
    print("you are sharon")
    print("hello")
    print("world")
elif my_name == "sharon":
    print("found your name")
else:
    print("efi")

print(a ==50)

should_i_work_today = a == 50 and b < 100
if should_i_work_today:
    print("go to work")
else:
    print("stay at home")

print("---------------------------------")


my_list = [0]
if my_list:
    print("you have items")
else:
    print("no items in the list")

string_ln = len("sghfdhjf")

print("---------------------------------")

my_other_list = ["or", "tohar", "adam", "moshe"]
my_other_nmae = "moshe"

if my_other_nmae in my_other_list:
    print("i found you")

print("---------------------------------")

# tt = "a"
# rr = "a"
# tt = 1
# rr = 1
tt = [1, 2, 3]
rr = [1, 2, 3]
print(tt is rr)
print(type(tt) is list)








