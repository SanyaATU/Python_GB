a = float(input('Результат в км: '))
b = float(input('Цель в км: '))
i = 1
d = a
while d < b:
    print(f'{i}-й день: {d:.2f}')
    d += round(0.1 * d, 2)
    i += 1
print(f'Ответ: на {i}-й день спортсмен достиг результата — не менее {b} км.')
