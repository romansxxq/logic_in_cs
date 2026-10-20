def fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


target = int(input("Яке число шукаємо? "))
limit = int(input("Скільки чисел перевірити? "))

found = False

for index, number in enumerate(fibonacci()):
    if index >= limit:
        break

    if number == target:
        print(f"Число знайдено на позиції {index}.")
        found = True
        break

if not found:
    print(f"Число не знайдено серед перших {limit} чисел.")
