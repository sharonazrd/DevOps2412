for i in range(5):
    print("hello " + str(i))
#    print("hello ", i)
else: #only if the for used all the items
    print("finished")


print("---------------------------------")

#for each
class_mates = ["maxim", "yoni", "gilad", "oren"]
for name in class_mates:
    if name == "yoni":
        name = "amir"
    print(name)
print(class_mates)

print("---------------------------------")

#by index
for i in range(len(class_mates)):
    print(class_mates[i])
print(class_mates)

print("---------------------------------")

your_name = input("enter your name: ")
while your_name != "sharon":
    print("you are not sharon")
    if your_name.lower() == "haim".lower():
        print("oh my god")
        break
    if your_name == "david":
        print("wow!")
#        continue
    your_name = input("enter your name: ")
else:
    print("your name is sharon")
