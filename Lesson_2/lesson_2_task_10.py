def bank(x, y):
    total = x  
    for _ in range(y):
        total += total * 0.1  
    return total

x = float(input("Введите сумму вклада: "))
y = int(input("Введите срок вклада в годах: "))

result = bank(x, y)
print("Сумма на счету пользователя спустя", y, "лет:", result, "рублей")
