def fact(number):
    x = 1
    for i in range(1, number + 1):
        x *= i
        yield x


n = 16
for ind, el in enumerate(fact(n)):
    print(f"{ind + 1} {el}")




