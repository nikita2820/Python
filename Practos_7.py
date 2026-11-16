# Задание 1
def say_hello():
    print("Привет, мир!")


say_hello()
say_hello()


# Задание 2
def greet(name):
    print(f"Привет, {name}!")


greet("Анна")
greet("Олег")


# Задание 3
def add(a, b):
    return a + b


result = add(3, 5)
print(result)


# Задание 4
def greet(name="Гость"):
    print(f"Привет, {name}!")


greet("Анна")
greet()


# Задание 5
def subtract(a, b):
    return a - b


print(subtract(10, 3))
print(subtract(a=10, b=3))
print(subtract(b=3, a=10))


# Задание 6
def introduce(name, city="Москва"):
    # Формы названий городов после слова «из».
    city_forms = {
        "Москва": "Москвы",
        "Казань": "Казани",
        "Омск": "Омска"
    }
    city_from = city_forms.get(city, city)
    return f"Меня зовут {name}, я из {city_from}"


print(introduce("Анна"))
print(introduce("Олег", "Казань"))


# Задание 7
def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(multiply(2, 3, 4))
print(multiply())


# Задание 8
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


display_info(имя="Анна", возраст=20, город="Москва")


# Задание 9
def order(product, quantity=1, *extras):
    result = f"Товар: {product}, количество: {quantity}"
    if extras:
        additions = ", ".join(str(item) for item in extras)
        result += f", дополнения: {additions}"
    return result


print(order("Пицца"))
print(order("Пицца", 2, "Сыр", "Грибы", "Соус"))


# Задание 10
def profile(name, age=18, **info):
    result = [f"Имя: {name}", f"Возраст: {age}"]
    for key, value in info.items():
        result.append(f"{key} — {value}")
    return result


print(profile("Анна"))
print(profile("Олег", 25, город="Омск", профессия="Программист"))
