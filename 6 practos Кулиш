# 1. Словарь учеников и оценок
students = {
    "Анна": 5,
    "Иван": 4,
    "Мария": 3
}
name = input("Введите имя ученика: ")
print(students.get(name, "Такого ученика нет"))


# 2. Добавление, изменение и удаление
data = {
    "a": 10,
    "b": 20,
    "c": 30
}
data["d"] = 40
data["a"] = 100
del data["b"]
print(data)


# 3. Значение по ключу
data = {
    "имя": "Анна",
    "возраст": 16
}
key = input("Введите ключ: ")
print(data.get(key, "Нет такого ключа"))


# 4. Все ключи, значения и количество пар
data = {
    "a": 10,
    "b": 20,
    "c": 30
}
print("Ключи:", list(data.keys()))
print("Значения:", list(data.values()))
print("Количество пар:", len(data))


# 5. Товары и цены
products = {
    "Хлеб": 50,
    "Молоко": 90,
    "Сыр": 250
}
for product, price in products.items():
    print(product, price)


# 6. Сумма цен и самый дорогой товар
products = {
    "Хлеб": 50,
    "Молоко": 90,
    "Сыр": 250
}
print("Сумма цен:", sum(products.values()))

print("Самый дорогой товар:", max(list(products.values())))


# 7. Количество каждого символа
text = input("Введите строку: ")
char_counts = {}

for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1

print(char_counts)


# 8. Количество каждого слова и самое частое слово
text = input("Введите слова через пробел: ")
word_counts = {}

for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
print("Самое частое слово:", max(list(word_counts.values())))


# 9. Поменять ключи и значения местами
data = {
    "a": 1,
    "b": 2,
    "c": 3
}
reversed_data = {}

for key, value in data.items():
    reversed_data[value] = key

print(reversed_data)


# 10. Страны и столицы
countries = ["Россия", "Франция", "Япония"]
capitals = ["Москва", "Париж", "Токио"]
country_capitals = dict(zip(countries, capitals))

country = input("Введите страну: ")
print(country_capitals.get(country, "Такой страны нет в словаре"))
