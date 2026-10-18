# ===== Цикл for =====

# 1. Числа от 1 до 10
for i in range(1, 11):
    print(i)

# 2. Чётные числа от 2 до 50
for i in range(2, 51, 2):
    print(i)

# 3. Числа от 10 до 1
for i in range(10, 0, -1):
    print(i)

# 4. Сумма чисел от 1 до n
n = int(input("n = "))
total = 0
for i in range(1, n + 1):
    total += i
print("Сумма:", total)

# 5. Факториал n
n = int(input("n = "))
result = 1
for i in range(2, n + 1):
    result *= i
print("Факториал:", result)

# 6. Таблица умножения на n
n = int(input("n = "))
for i in range(1, 11):
    print(n, "*", i, "=", n * i)

# 7. Количество положительных чисел в списке
numbers = [3, -1, 0, 5, -7, 8, -2, 4]
count = 0
for x in numbers:
    if x > 0:
        count += 1
print("Положительных:", count)

# 8. Количество гласных в строке
text = input("Строка: ")
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Гласных:", count)

# 9. Наибольший элемент без max()
numbers = [3, 17, -4, 9, 25, 0, 12]
biggest = numbers[0]
for x in numbers:
    if x > biggest:
        biggest = x
print("Наибольший:", biggest)

# 10. Таблица умножения 9x9 в виде квадрата
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print()
