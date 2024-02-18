details = ["sharon", "azrad", 50, True]
details_dict = {"fname": "sharon",
                "lname": "azrad",
                "age": 50,
                "is_married": True}

print(details_dict.keys())
print(details_dict.values())

print("---------------------------------")

my_class = [
    {"fname": "or", "lname": "shemesh"},
    {"fname": "maxim", "lname": "levi"}
]
for student in my_class:
    print(student["fname"])

print("---------------------------------")



my_other_dict = {
    0: "moshe",
    1: "haim",
    2: 35,
    3: False
}
