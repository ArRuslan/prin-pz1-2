from __future__ import annotations

import inspect
import re
import time
from collections import Counter
from contextlib import contextmanager
from functools import wraps
from typing import Callable, NoReturn, Generator, Any


def task_a1_generator(arr: list[int]) -> Generator[int, None, None]:
    for el in arr:
        if el % 2 == 0:
            yield el


def task_a1() -> None:
    """Написати генератор, який повертає тільки парні числа зі списку"""
    numbers = map(int, input("Numbers: ").split(" "))
    for num in task_a1_generator(list(numbers)):
        print(num)


def task_a2() -> None:
    """Написати генератор паролів заданої довжини (формат: 1+ символ алфавіту, 1+ цифра, 1+ спецсимвол)."""
    # TODO


def task_a3() -> None:
    """Написати ітератор і генератор, який на вхід приймає масив рядків, а повертає масив, кожен елемент якого є масивом байт перераховується елементу."""
    # TODO


def task_a4_generator(arr: list[str], ln: int) -> Generator[str, None, None]:
    for el in arr:
        if len(el) == ln:
            yield el


def task_a4() -> None:
    """Написати генератор, який на вхід отримує список рядків і повертає рядки, довжина яких дорівнює заданої."""
    words = input("Words: ").split(" ")
    for s in task_a4_generator(words, 5):
        print(s)


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


def task_b5_dec(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        args = list(sorted(args))
        print(f"Sorted arguments: {args}")
        args = filter(lambda arg: arg >= 0, args)

        return func(*args, **kwargs)

    return wrapper


@task_b5_dec
def task_b5_func(*args: int) -> None:
    print(f"Arguments: {args}")


def task_b5() -> None:
    """Написати декоратор, який перед виконанням функції виводить відсортований список її аргументів, а потім виконує функцію лише з її позитивними аргументами"""
    task_b5_func(9, -8, 7, 6, 5, -4, 3, -2, -1)


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
    fib = lambda n: (1 if n in (1, 2) else fib(n - 1) + fib(n - 2))

    print(fib(10))


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


class ClassAttrsToDict:
    def __init__(self) -> None:
        self._dict = {}

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "_dict":
            self.__dict__[key] = value
            return
        self.__dict__["_dict"][key] = value

    def __getattr__(self, item: str) -> Any:
        return self.__dict__["_dict"][item]


def task_d5() -> None:
    """Реалізувати клас, який під час запису значення атрибута, поміщає його в поле-dict, де ключ - ім'я атрибута"""
    obj = ClassAttrsToDict()
    obj.a = 1
    obj.b = 2
    obj.c = 3

    print(f"{obj.a=}")
    print(f"{obj.b=}")
    print(f"{obj.c=}")

    print(f"{obj._dict=}")


def task_e1() -> None:
    """Розбити рядок на список по символ пробілу (скільки завгодно поспіль)"""
    text = input("Text: ")
    result = re.split(r"\s+", text)
    print(result)


def task_e2() -> None:
    """Перевірити вірність номера кредитної картки"""
    card = input("Card number: ")
    result = re.match(r"^\d{16}$", card)
    print("Valid" if result is not None else "Invalid")


def task_e3() -> None:
    """Витягти дати з рядка"""
    # 12.12.2000 asd 123 qwe 12.02.2000 asd 31.02.2000 asd
    text = input("Text: ")
    for date in re.findall(r"((?:(?:(?:(?:[01]\d)|(?:2[0-8]))\.02)|(?:(?:[012]\d)|(?:3[01]))\.(?:(?:0[13456789])|(?:1[012])))\.\d{4})", text):
        print(date)


def task_e4() -> None:
    """Перевірити правильність введення e-mail"""
    card = input("Email: ")
    result = re.match(r"^[a-zA-Z\d_-]{1,254}@[a-zA-Z\d_-]{2,255}.[a-zA-Z]{2,20}$", card)
    print("Valid" if result is not None else "Invalid")


def task_e5() -> None:
    """Перевірити валідність українського мобільного номера (починається з "0", 10 цифр або починається з "+380", 13 цифр)"""
    card = input("Phone number: ")
    result = re.match(r"^((?:0\d{9})|(?:\+380\d{9}))$", card)
    print("Valid" if result is not None else "Invalid")


class BinaryTreeNode:
    def __init__(self, value: int, left: BinaryTreeNode | None = None, right: BinaryTreeNode | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeIterator:
    def __init__(self, tree: BinaryTreeNode) -> None:
        #self._tree = tree
        self._current = tree
        self._stack: list[BinaryTreeNode] = []

    def __iter__(self) -> BinaryTreeIterator:
        return self

    def __next__(self) -> int:
        while self._current is not None:
            self._stack.append(self._current)
            self._current = self._current.left

        if not self._stack:
            raise StopIteration

        self._current = self._stack.pop(0)
        node, self._current = self._current, self._current.right

        return node.value



def task_f1() -> None:
    """Реалізувати ітератор по бінарному дереву"""
    tree = BinaryTreeNode(
        1,
        BinaryTreeNode(2),
        BinaryTreeNode(3, BinaryTreeNode(4)),
    )

    for node in BinaryTreeIterator(tree):
        print(node)


class ValidatedArg:
    _DEFAULT_MISSING = object()

    def __init__(
            self, type_: type | None = None, gt: int | None = None, lt: int | None = None,
            min_len: int | None = None, max_len: int | None = None, default: Any | None = _DEFAULT_MISSING,
            nullable: bool | None = None,
    ) -> None:
        self.type = type_
        self.gt = gt
        self.lt = lt
        self.min_len = min_len
        self.max_len = max_len
        self.default = default
        self.nullable = nullable or default is None

    def check(self, value: Any) -> None:
        if self.type is not None:
            if not isinstance(value, (self.type,) if not self.nullable else (self.type, type(None),)):
                raise TypeError(f"Argument has invalid type: expected {self.type.__name__}, got {value.__class__.__name__}")
        if not self.nullable and value is None:
            raise TypeError(f"Non-nullable argument is None")

        if self.gt is not None and value is not None and value <= self.gt:
            raise ValueError(f"Argument must be bigger than {self.gt}")
        if self.lt is not None and value >= self.lt:
            raise ValueError(f"Argument must be less than {self.lt}")

        if self.min_len is not None and value is not None and len(value) < self.min_len:
            raise ValueError(f"Argument length must be bigger (or equal) than {self.min_len}")
        if self.max_len is not None and value is not None and len(value) > self.max_len:
            raise ValueError(f"Argument length must be less (or equal) than {self.max_len}")


def validated_func(func: Callable) -> Callable:
    sig = inspect.signature(func)
    validators: dict[str, ValidatedArg] = {
        name: param.default
        for name, param in sig.parameters.items()
        if isinstance(param.default, ValidatedArg)
    }
    annotations_ = inspect.get_annotations(func, eval_str=True)
    for name, validator in validators.items():
        if name not in annotations_:
            continue
        validator.type = annotations_[name]

    for name, ann in annotations_.items():
        if name in validators:
            continue
        validators[name] = ValidatedArg(ann)

    @wraps(func)
    def wrapper(*args, **kwargs) -> ...:
        bound = sig.bind_partial(*args, **kwargs)
        for arg in sig.parameters.keys():
            val = validators.get(arg)
            if arg not in bound.arguments and (val is None or val.default is val._DEFAULT_MISSING):
                raise ValueError(f"Missing argument: {arg}")
            if arg not in bound.arguments:
                bound.arguments[arg] = val.default

            if val is not None:
                val.check(bound.arguments[arg])

        return func(*bound.args, **bound.kwargs)

    return wrapper


@validated_func
def task_f2_func(int_arg: int, str_arg: str = ValidatedArg(max_len=10, default=None), arr_arg: list = ValidatedArg(min_len=1)) -> None:
    print(f"{int_arg=}, {str_arg=}, {arr_arg=}")


@contextmanager
def should_raise(exc_type: type[Exception]) -> Generator[None, None, None]:
    try:
        yield
    except exc_type as e:
        print(f"Exception was indeed raised: {exc_type.__name__}: {e}")
    else:
        print(f"Exception was NOT raised: {exc_type.__name__}")


def task_f2() -> None:
    """Реалізувати декоратор (з параметром), перевіряючий параметри функції на правильність (не тільки на тип, а, наприклад, порожнечу, діапазон значень і інші більш цікаві валідатори)"""
    task_f2_func(1, "asd", [123, 456])
    task_f2_func(1, arr_arg=[123, 456])
    task_f2_func(1, arr_arg=[123])

    with should_raise(TypeError):
        task_f2_func("1", "asd", [123, 456])
    with should_raise(ValueError):
        task_f2_func(1, arr_arg=[])
    with should_raise(ValueError):
        task_f2_func(1, "test")
    with should_raise(ValueError):
        task_f2_func(1, "testtesttest", [1])


def task_f3() -> None:
    """Перевірка рядка, що складається з нулів і одиниць, на наявність в ній парного кількості нулів і парного кількості одиниць за допомогою регулярного виразу"""
    # TODO


class _DisallowInheritanceMeta(type):
    def __new__(meta, name, bases, class_dict) -> NoReturn:
        if not bases:
            return type.__new__(meta, name, bases, class_dict)
        raise RuntimeError(f"You cant use {name} as a superclass!")


class ClassWithoutChildClasses(metaclass=_DisallowInheritanceMeta):
    def __init__(self) -> None:
        self.a = 1


def task_f4() -> None:
    """Заборонити наслідування класів"""
    try:
        class ThisShouldFail(ClassWithoutChildClasses):
            ...
    except RuntimeError as e:
        print(f"Error was indeed raised: {e.__class__.__name__}: {e}")


def main() -> None:
    task_funcs = (
        #task_a1, task_a2, task_a3, task_a4, task_a5,
        #task_b1, task_b2, task_b3, task_b4, task_b5,
        #task_c1, task_c2, task_c3, task_c4, task_c5,
        task_d1, task_d2, task_d3, task_d4, task_d5,
        #task_e1, task_e2, task_e3, task_e4, task_e5,
        #task_f1, task_f2, task_f3, task_f4,

        #task_b5,
    )

    for task_func in task_funcs:
        print(f"Task {task_func.__name__.split('_')[1].upper()}")
        try:
            task_func()
        except Exception as e:
            print(f"Task raised exception: {e.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()
