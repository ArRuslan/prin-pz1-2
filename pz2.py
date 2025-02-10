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


def task_b1() -> None:
    """Написати декоратор, який перед виконанням функції виводить "here is a simple function", а після неї - "eventually, it ended\""""
    # TODO


def task_b2() -> None:
    """Декоратор для обробки винятків (зловити виключення з функції і викинути загальне назовні)"""
    # TODO


def task_b3() -> None:
    """Написати декоратор, який виводить час виконання функції"""
    # TODO


def task_b4() -> None:
    """Написати декоратор, який простий текст зробить html розміткою"""
    # TODO


def task_b5() -> None:
    """Написати декоратор, який перед виконанням функції виводить відсортований список її аргументів, а потім виконує функцію лише з її позитивними аргументами"""
    # TODO


def task_c1() -> None:
    """Дана рядок. Вивести на екран частоту слів у тексті у вигляді "слово: частота\""""
    # TODO


def task_c2() -> None:
    """Звести кожен елемент списку в куб (з допомогою map)"""
    # TODO


def task_c3() -> None:
    """Фільтрувати позитивні елементи списку (за допомогою filter)"""
    # TODO


def task_c4() -> None:
    """Конвертувати список оцінок з 100-бальною в 5-бальну шкалу (map)"""
    # TODO


def task_c5() -> None:
    """Визначити лямбда-функцію для отримання числа Фібоначчі за його індексом."""
    # TODO


def task_d1() -> None:
    """Реалізувати клас з методами для обчислення площі та периметра прямокутника"""
    # TODO


def task_d2() -> None:
    """Реалізувати клас, який при зверненні до атрибуту повертає ім'я типу атрибута у верхньому регістрі"""
    # TODO


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
        task_a1, task_a2, task_a3, task_a4, task_a5,
        task_b1, task_b2, task_b3, task_b4, task_b5,
        task_c1, task_c2, task_c3, task_c4, task_c5,
        task_d1, task_d2, task_d3, task_d4, task_d5,
        task_e1, task_e2, task_e3, task_e4, task_e5,
        task_f1, task_f2, task_f3, task_f4,
    )

    for task_func in task_funcs:
        print(f"Task {task_func.__name__.split('_')[1].upper()}")
        task_func()


if __name__ == "__main__":
    main()
