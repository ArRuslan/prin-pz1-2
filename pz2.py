import time
from collections import Counter
from functools import wraps
from typing import Callable


def task_a1() -> None:
    """Написати генератор, який повертає тільки парні числа зі списку"""
    # TODO


def task_a2() -> None:
    """Написати генератор паролів заданої довжини (формат: 1+ символ алфавіту, 1+ цифра, 1+ спецсимвол)."""
    # TODO


def task_a3() -> None:
    """Написати ітератор і генератор, який на вхід приймає масив рядків, а повертає масив, кожен елемент якого є масивом байт перераховується елементу."""
    # TODO


def task_a4() -> None:
    """Написати генератор, який на вхід отримує список рядків і повертає рядки, довжина яких дорівнює заданої."""
    # TODO


def task_a5() -> None:
    """Написати генератор, який повертає список чисел, у яких сума цифр дорівнює заданому числу"""
    # TODO


def task_b1_dec(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> ...:
        print("here is a simple function")
        result = func(*args, **kwargs)
        print("eventually, it ended")

        return result

    return wrapper


@task_b1_dec
def task_b1() -> None:
    """Написати декоратор, який перед виконанням функції виводить "here is a simple function", а після неї - "eventually, it ended\""""
    print("in function")


def task_b2_dec(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> ...:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise Exception

    return wrapper


@task_b2_dec
def task_b2() -> None:
    """Декоратор для обробки винятків (зловити виключення з функції і викинути загальне назовні)"""
    raise RuntimeError("some runtime error")


def task_b3_dec(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> ...:
        time_start = time.time()
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} was running for {time.time() - time_start:.2f} seconds")

        return result

    return wrapper


@task_b3_dec
def task_b3() -> None:
    """Написати декоратор, який виводить час виконання функції"""
    time.sleep(3)


def task_b4_dec(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        result = func(*args, **kwargs)
        paragraphs = map(lambda line: f"  <p>{line}</p>", result.split("\n"))
        paragraphs = "\n".join(paragraphs)

        return f"<html>\n<body>\n{paragraphs}\n</body>"

    return wrapper


@task_b4_dec
def task_b4_some_text() -> str:
    return (
        "first line\n" +
        "second line\n" +
        "third line"
    )


def task_b4() -> None:
    """Написати декоратор, який простий текст зробить html розміткою"""
    print(task_b4_some_text())


def task_b5() -> None:
    """Написати декоратор, який перед виконанням функції виводить відсортований список її аргументів, а потім виконує функцію лише з її позитивними аргументами"""
    # TODO


def task_c1() -> None:
    """ Дан рядок. Вивести на екран частоту слів у тексті у вигляді "слово: частота" """
    text = input("String: ")
    for word, count in Counter(text.split()).items():
        print(f"{word}: {count}")


def task_c2() -> None:
    """Звести кожен елемент списку в куб (з допомогою map)"""
    nums = input("Numbers: ")
    pow_of_3 = map(lambda num: num ** 3, map(int, nums.split(" ")))
    pow_of_3_str = map(str, pow_of_3)

    print(" ".join(pow_of_3_str))


def task_c3() -> None:
    """Фільтрувати позитивні елементи списку (за допомогою filter)"""
    nums = input("Numbers: ")
    positive = filter(lambda num: num >= 0, map(int, nums.split(" ")))
    positive_str = map(str, positive)

    print(" ".join(positive_str))


def task_c4() -> None:
    """Конвертувати список оцінок з 100-бальною в 5-бальну шкалу (map)"""
    nums = input("Grades: ")
    grades_5 = map(lambda num: num // 20, map(int, nums.split(" ")))
    grades_5_str = map(str, grades_5)

    print(" ".join(grades_5_str))


def task_c5() -> None:
    """Визначити лямбда-функцію для отримання числа Фібоначчі за його індексом."""
    # TODO


class Rectangle:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def get_area(self) -> int:
        return self.a * self.b

    def get_perimeter(self) -> int:
        return self.a * 2 + self.b * 2


def task_d1() -> None:
    """Реалізувати клас з методами для обчислення площі та периметра прямокутника"""
    rect = Rectangle(4, 5)
    print(f"Area of rectangle 4x5: {rect.get_area()}")
    print(f"Perimeter of rectangle 4x5: {rect.get_perimeter()}")


class GetAttributeTypeName:
    def __init__(self) -> None:
        self.a = 1
        self.b = ""
        self.c = None
        self.d = 42.
        self.e = []
        self.f = {}
        self.g = Rectangle(1, 1)

    def __getattribute__(self, item: str) -> str:
        attr = object.__getattribute__(self, item)
        return type(attr).__name__.upper()


def task_d2() -> None:
    """Реалізувати клас, який при зверненні до атрибуту повертає ім'я типу атрибута у верхньому регістрі"""
    obj = GetAttributeTypeName()
    print(f"{obj.a=}")
    print(f"{obj.b=}")
    print(f"{obj.c=}")
    print(f"{obj.d=}")
    print(f"{obj.e=}")
    print(f"{obj.f=}")
    print(f"{obj.g=}")


def task_d3() -> None:
    """Реалізувати клас з методами повертають текст в різних форматах."""
    # TODO


def task_d4() -> None:
    """Реалізувати шаблон проектування Command"""
    # TODO


def task_d5() -> None:
    """Реалізувати клас, який під час запису значення атрибута, поміщає його в поле-dict, де ключ - ім'я атрибута"""
    # TODO


def task_e1() -> None:
    """Розбити рядок на список по символ пробілу (скільки завгодно поспіль)"""
    # TODO


def task_e2() -> None:
    """Перевірити вірність номера кредитної картки"""
    # TODO


def task_e3() -> None:
    """Витягти дати з рядка"""
    # TODO


def task_e4() -> None:
    """Перевірити правильність введення e-mail"""
    # TODO


def task_e5() -> None:
    """Перевірити валідність українського мобільного номера (починається з "0", 10 цифр або починається з "+380", 13 цифр)"""
    # TODO


def task_f1() -> None:
    """Реалізувати ітератор по бінарному дереву"""
    # TODO


def task_f2() -> None:
    """Реалізувати декоратор (з параметром), перевіряючий параметри функції на правильність (не тільки на тип, а, наприклад, порожнечу, діапазон значень і інші більш цікаві валідатори)"""
    # TODO


def task_f3() -> None:
    """Перевірка рядка, що складається з нулів і одиниць, на наявність в ній парного кількості нулів і парного кількості одиниць за допомогою регулярного виразу"""
    # TODO


def task_f4() -> None:
    """Заборонити наслідування класів"""
    # TODO


def main() -> None:
    task_funcs = (
        #task_a1, task_a2, task_a3, task_a4, task_a5,
        #task_b1, task_b2, task_b3, task_b4, task_b5,
        #task_c1, task_c2, task_c3, task_c4, task_c5,
        task_d1, task_d2, task_d3, task_d4, task_d5,
        #task_e1, task_e2, task_e3, task_e4, task_e5,
        #task_f1, task_f2, task_f3, task_f4,
    )

    for task_func in task_funcs:
        print(f"Task {task_func.__name__.split('_')[1].upper()}")
        try:
            task_func()
        except Exception as e:
            print(f"Task raised exception: {e.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()
