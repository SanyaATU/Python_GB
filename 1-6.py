a = float(input("Результат в км: "))
b = float(input("Цель в км: "))
i = 1
while a < b:
    a *= 1.1
    i += 1
print(f"Цель будет достигнута на {i}-й день")
