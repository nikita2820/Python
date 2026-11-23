# Задание 1
# Сохраняем функцию в переменную и вызываем через неё.

def say_hi():
    print("Привет!")


other = say_hi
other()


# Задание 2
# Два имени ссылаются на одну функцию.

def cube(x):
    return x ** 3


cube_first = cube
cube_second = cube

print(cube_first(2))   # 8
print(cube_second(3))  # 27


# Задание 3
# Сравниваем тип функции и тип результата её вызова.

def get_five():
    return 5


print(type(get_five))    # <class 'function'>
print(type(get_five()))  # <class 'int'>


# Задание 4
# Передаём функцию приветствия другой функции.

def greeting():
    print("Здравствуйте!")


def run(action):
    action()


run(greeting)


# Задание 5
# Передаём функцию удвоения и число 6.

def double(number):
    return number * 2


def apply(action, number):
    return action(number)


print(apply(double, 6))  # 12


# Задание 6
# Применяем переданную функцию к каждому элементу списка.

def add_ten(number):
    return number + 10


def transform(values, action):
    return [action(value) for value in values]


print(transform([1, 2, 3], add_ten))  # [11, 12, 13]


# Задание 7
# Возвращаем функцию и затем вызываем её.

def factory():
    def action():
        print("Работает")

    return action


created_function = factory()
created_function()


# Задание 8
# Возвращённая функция запоминает значение value.

def make_adder(value):
    def adder(number):
        return number + value

    return adder


add_five = make_adder(5)
print(add_five(7))  # 12


# Задание 9
# Каждый вызов счётчика возвращает следующее число.

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter = make_counter()

print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
