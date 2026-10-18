import random

# ===== Цикл while =====

# 1. Числа от 1 до 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Вводим числа, пока не введён 0, выводим сумму
total = 0
x = int(input("Число: "))
while x != 0:
    total += x
    x = int(input("Число: "))
print("Сумма:", total)

# 3. Количество цифр в числе
n = int(input("Число: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Цифр:", count)

# 4. Сумма цифр числа
n = int(input("Число: "))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Сумма цифр:", total)

# 5. Цифры в обратном порядке одним числом
n = int(input("Число: "))
result = 0
while n > 0:
    result = result * 10 + n % 10
    n //= 10
print("Наоборот:", result)

# 6. Степени двойки, не превышающие n
n = int(input("n = "))
p = 1
while p <= n:
    print(p)
    p *= 2

# 7. Запрашивать пароль, пока не введён правильный
password = "qwerty"
attempt = input("Пароль: ")
while attempt != password:
    print("Неверно")
    attempt = input("Пароль: ")
print("Верно")

# 8. НОД двух чисел
a = int(input("a = "))
b = int(input("b = "))
while b != 0:
    a, b = b, a % b
print("НОД:", a)

# 9. Числа Фибоначчи, не превышающие n
n = int(input("n = "))
a, b = 0, 1
while a <= n:
    print(a)
    a, b = b, a + b

# 10. Игра «Угадай число»
secret = random.randint(1, 100)
attempts = 0
guess = 0
while guess != secret:
    guess = int(input("Ваше число: "))
    attempts += 1
    if guess < secret:
        print("больше")
    elif guess > secret:
        print("меньше")
print("Угадали! Попыток:", attempts)
