a = float(input("Выручка: "))
b = float(input("Издержки: "))
if a > b:
    print("Прибыльное дело")
    print(f"Рентабельность: {a / b:.2f}")
    c = int(input("Кол-во сотрудников: "))
    print(f"Прибыль на каждого сотрудника:  {a / c:.2f}")
elif a == b:
    print("Работаем в ноль")
else:
    print("Невыгодное дело")