import datetime
import time
start_time = time.monotonic()
user_input = input("Введите комманду и числа оперции: ")
"""Ввод пользователем поочередно: сначала функция => потом два числа"""
input_list = user_input.split(" ")
"""Разбитие ввода на части через пробел"""

try:
    """Проверка условий ввода и приравнивание к integers чисел"""
    mark = (input_list[0])
    a = int(input_list[1])
    b = int(input_list[2])
    if mark == "+":
        result = a + b
    elif mark == "/":
        result = a / b
    elif mark == "-":
        result = a - b
    elif mark == "*":
        result = a * b
    print(result)
    """Проверка на шибки ввода - /0, ввод букв вместо чисел, недостаточное количество чисел"""
except ZeroDivisionError as Z:
    print(Z, type(Z))
    print("Делить на ноль нельзя!")
except ValueError as V:
    print(V, type(V))
    print("Неверный ввод данных")
except IndexError as I:
    print(I, type(I))
    print("Маловато операндов")
finally:
    print("Этот блок будет выполнятся всегда")


class loger:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, "a", encoding="utf8")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.file.write(f'\n {datetime.datetime.now()} Ошибка {exc_type} {exc_val}\n')
        self.file.close()

    def write_in_log(self):
        self.file.write(f"\n INFO {datetime.datetime.now()} \n")


class Except:
    def __init__(self, exp):
        self.exp = exp


if __name__ == 'main':
    log = loger('log.txt')
    with loger('log.txt') as log:
        log.write_in_log()
        print(log)
