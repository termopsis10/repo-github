def my_func(arg_1, arg_2, arg_3):
    if arg_1 >=arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_1 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3

print(f"Result  {my_func(int(input('введите первый аргумент: ')), int(input('введите второй аргумент: ')), int(input('введите третий аргумент: ')) )}")
