def add_3_names():
    my_file = open("names.txt","a+")
    for i in range(3):
        name = "\n" + input(f"add name # {i+1} : ")
        my_file.writelines(name)

def print_names():
    my_file = open("names.txt","r")
    for name in my_file.readlines():
        print(f"hello {name}", end='')


add_3_names()
print_names()
