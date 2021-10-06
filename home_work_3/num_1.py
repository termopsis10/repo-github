def my_div(num_1, num_2):
    if num_2 == 0:
        return " ошибочная операция"
    else:
        return num_1 / num_2

num_1 = int(input("num_1:  "))
num_2 = int(input("num_2:  "))
print(my_div(num_1, num_2))