def my_func(name, surname, year, city, email, phone):
    print(f"{name} {surname} {year} {city} {email} {phone}")
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите почту: ")
phone = input("Введите номер телефона: ")
my_func(name = name, surname = surname, year = year, city = city, email = email, phone = phone)
