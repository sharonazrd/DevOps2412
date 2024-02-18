# for i in range(5):
#     print("hello " + str(i))
#
# for i in range(10):
#     print("you are number " + str(i))
#
# print("---------------------------------")

def my_printer(prefix, amount_of_times):
    for i in range(amount_of_times):
        print(prefix + str(i))


def mul_five(my_number):
    result = my_number * 5
    return result

the_result = mul_five(10)
print(the_result)

if mul_five(10) > 1:
    my_printer("hello ", 5)
#my_printer("you are number ", 10)
