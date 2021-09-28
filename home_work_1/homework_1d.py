a = int(input("Расстояние в км за 1-ый день "))
b = int(input("Желаемый результат в км "))
days = 1
km = a
while km < b:
    a = a + (a / 10)
    days = days + 1
    km = km + (a/10)
print("Потрачено дней для достижения цели ", days)
