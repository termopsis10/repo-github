def int_fuc(txt):
    word =int_fuc(txt.capitalize())
    return word

string = input(' Введите строку разделенную пробелами: ')
for word in string.split(' '):
    print(f'{int_func(word)}', end=' ')
