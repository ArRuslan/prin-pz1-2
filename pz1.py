import math
import random
from collections import Counter
from datetime import date


def task_a1() -> None:
    """Вивести на екран прямокутник, заповнений літерами А. Кількість рядків в прямокутнику одно 5, кількість стовпців дорівнює 8."""
    width = 8
    height = 5

    for _ in range(height):
        print("A" * width)


def task_a2() -> None:
    """Вивести на екран букву "W" з символів "*" (зірочка)."""
    # TODO


def task_a3() -> None:
    """Вивести на екран поточну назву дня тижня, назву місяця і своє ім'я. Кожне слово має бути в окремому рядку."""
    today = date.today()

    print(today.strftime("%A"))
    print(today.strftime("%B"))
    print("Ruslan")


def _input_number(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            ...


def task_b1() -> None:
    """ Користувач вводить суму вкладу в банк і річний відсоток. Знайдіть суму вкладу через 5 років """
    initial_deposit = _input_number("Initial deposit: ")
    percent_per_year = _input_number("Per year (%): ")
    per_year = 1 + percent_per_year / 100

    after_five_years = initial_deposit
    for _ in range(5):
        after_five_years *= per_year

    print(f"After 5 years: {after_five_years}")


def task_b2() -> None:
    """ Дано значення температури в градусах Цельсія. Вивести температуру в градусах Фаренгейта """
    temp = _input_number("Temperature (C): ")
    print(f"In fahrenheit: {temp * 9 / 5 + 32:.2f}")


def task_b3() -> None:
    """ Користувач вводить кількість тижнів, місяців, років і отримує кількість днів за цей час. Вважати, що в місяці 30 днів """
    weeks = _input_number("Weeks: ")
    months = _input_number("Months: ")
    years = _input_number("Years: ")

    print(f"Total days: {weeks * 7 + months * 30 + years * 365}")


def task_c1() -> None:
    """ Дана дата із трьох чисел (день, місяць і рік). Вивести yes, якщо така дата існує (наприклад, 12 02 1999 - yes, 22 13 2001 - no). Вважати, що в лютому завжди 28 днів """
    date_ = input("Date: ").strip().split(" ")
    try:
        day, month, year = date_
        day = int(day)
        month = int(month)
        int(year)
    except ValueError:
        print("Invalid date!")
        return

    if month > 12:
        print(f"Invalid date: month > 12")

    max_days = 31
    if month == 2:
        max_days = 28
    elif month in (4, 6, 9, 11):
        max_days = 31

    if day > max_days:
        print(f"Invalid date: max number of days is {max_days}")

    print("yes")


def task_c2() -> None:
    """ Дано чотиризначний число. Чи вірно, що цифри в ньому розташовані за зменшенням? Наприклад, 4311 - немає, 4321 - да, 5542 - немає, 5631 - немає, 9871 - так """
    num = _input_number("Number: ")
    last = -1
    while num > 0:
        current = num % 10
        num //= 10
        if current <= last:
            print("no")
            return

    print("yes")


def _swap_numbers(num: int, pos1: int, pos2: int) -> int:
    num_at_pos1 = (num // (10 ** pos1)) % 10
    num_at_pos2 = (num // (10 ** pos2)) % 10

    num -= num_at_pos1 * (10 ** pos1)
    num -= num_at_pos2 * (10 ** pos2)

    num += num_at_pos2 * (10 ** pos1)
    num += num_at_pos1 * (10 ** pos2)

    return num


def task_c3() -> None:
    """ Дано чотиризначне число. Поміняйте місцями найменшу і найбільшу цифри """
    num = _input_number("Number: ")
    result = num

    mx = 0
    mn = 9
    mx_pos = mn_pos = 0
    pos = 0

    while num > 0:
        current = num % 10
        num //= 10

        if current > mx:
            mx = current
            mx_pos = pos

        if current < mn:
            mn = current
            mn_pos = pos

        pos += 1

    result = _swap_numbers(result, mx_pos, mn_pos)
    print(result)


def task_c4() -> None:
    """ Дано числа h і m, де h - кількість годин, m - кількість хвилин деякого моменту часу. Знайдіть кут між годинниковою та хвилинною стрілками в цей момент часу """
    hours = _input_number("H: ")
    minutes = _input_number("M: ")

    minutes_angle = minutes * 360 / 60
    hours_angle = hours * 360 / 12 + minutes_angle / 12

    print(abs(hours_angle - minutes_angle))


def task_c5() -> None:
    """ Дано чотиризначне число. Переставте місцями цифри так, щоб спочатку виявилися цифри, менші п'яти """
    num = _input_number("4-digit number: ")

    pos_to_swap = 3
    for pos in range(3, -1, -1):
        dig = (num // (10 ** pos)) % 10
        if dig < 5:
            if pos != pos_to_swap:
                num = _swap_numbers(num, pos, pos_to_swap)
            pos_to_swap -= 1

    print(num)


def task_d1() -> None:
    """ Вивести на екран числа від 1000 до 9999 такі, що всі цифри різнi """
    for i in range(1000, 9999 + 1):
        unique = True
        for pos in range(4):
            num = (i // (10 ** pos)) % 10
            for check_pos in range(pos + 1, 4):
                if (i // (10 ** check_pos)) % 10 == num:
                    unique = False
                    break

            if not unique:
                break

        if unique:
            print(i)


def task_d2() -> None:
    """ Вивести на екран числа від 1000 до 9999 такі, що серед чисел є цифра 3 """
    for i in range(1000, 9999 + 1):
        has_3 = False
        for pos in range(4):
            num = (i // (10 ** pos)) % 10
            if num == 3:
                has_3 = True
                break

        if has_3:
            print(i)


def task_d3() -> None:
    """ Виведіть на екран квадрат з нулів й одиниць, причому нулі знаходяться тільки на діагоналі квадрата. Всього в квадраті сто цифр """
    a = 10

    for i in range(a):
        for j in range(a):
            print(0 if i == j else 1, end=" ")

        print()


def task_d4() -> None:
    """ Згенерувати випадкову серію з 15 чисел, в якій рівно 3 одиниці, інші нулі """
    total_nums = 15
    ones = 3
    nums = [
        *(1 for _ in range(ones)),
        *(0 for _ in range(total_nums - ones))
    ]
    random.shuffle(nums)

    print("".join(map(str, nums)))


def task_d5() -> None:
    """ Комп'ютер загадує число від 1 до 100. У користувача три спроби відгадати. Після кожної невдалої спроби комп'ютер повідомляє менше або більше загадане число """
    num = random.randint(1, 100)

    for i in range(3):
        user_num = _input_number(f"Guess {i}: ")
        if num == user_num:
            print("Correct!")
            return
        if num > user_num:
            print("Bigger")
        else:
            print("Smaller")

    print(f"Number was {num}")


def task_e1() -> None:
    """ Створити масив, кожен елемент якого дорівнює квадрату свого номера """
    elements_num = _input_number("Number of elements: ")
    print([i * i for i in range(elements_num)])


def task_e2() -> None:
    """ Сформувати масив з випадкових чисел, в яких рівно дві одиниці, стоять на випадкових позиціях """
    elements_num = _input_number("Number of elements: ")
    choices = list(range(0, 10))
    del choices[1]

    arr = [random.choice(choices) for _ in range(elements_num)]
    idx1 = idx2 = random.randint(0, len(arr) - 1)
    while idx1 == idx2:
        idx2 = random.randint(0, len(arr) - 1)

    arr[idx1] = arr[idx2] = 1

    print(arr)


def task_e3() -> None:
    """ Заповніть масив випадковим чином нулями й одиницями так, щоб кількість одиниць було більше кількості нулів """
    elements_num = _input_number("Number of elements: ")
    ones = math.ceil(elements_num * 0.51)
    nums = [
        *(1 for _ in range(ones)),
        *(0 for _ in range(elements_num - ones))
    ]
    random.shuffle(nums)

    print(nums)


def task_e4() -> None:
    """ В даному масиві знайти максимальну кількість однакових елементів """
    nums = map(int, input("Numbers: ").split(" "))
    counter = Counter(nums)
    most_common = counter.most_common(1)
    if most_common:
        print(most_common[0][0])


def task_e5() -> None:
    """ Дан масив. Сформувати новий масив, в якому йдуть спочатку негативні елементи, потім нулі, потім позитивні """
    nums = map(int, input("Numbers: ").split(" "))
    result = []

    negative_idx = 0
    zero_idx = 0
    positive_idx = 0

    for num in nums:
        if num < 0:
            result.insert(negative_idx, num)
            negative_idx += 1
            zero_idx += 1
            positive_idx += 1
        elif num > 0:
            result.insert(positive_idx, num)
            positive_idx += 1
        else:
            result.insert(zero_idx, num)
            zero_idx += 1
            positive_idx += 1

    print(result)


def _gen_matrix_of_size(n: int) -> list[list[int]]:
    choices = list(range(0, 10))
    return [
        random.choices(choices, k=n) for _ in range(n)
    ]


def _print_mat(mat: list[list[int]]) -> None:
    for row in mat:
        print(" ".join(map(str, row)))


def _print_mat_col(mat: list[list[int]], col: int) -> None:
    for row in mat:
        print(row[col], end=" ")

    print()


def task_f1() -> None:
    """ Дана матриця. Вивести на екран всі непарні стовпці, у яких перший елемент більше останнього """
    matrix_size = 5
    mat = _gen_matrix_of_size(matrix_size)

    print("Matrix: ")
    _print_mat(mat)

    for col in range(0, matrix_size, 2):
        if mat[0][col] > mat[matrix_size - 1][col]:
            print(f"Column [{col}]: ", end="")
            _print_mat_col(mat, col)


def task_f2() -> None:
    """ Дана матриця. Вивести k-й рядок і p-й стовпець матриці """
    matrix_size = 5
    mat = _gen_matrix_of_size(matrix_size)

    print("Matrix: ")
    _print_mat(mat)

    row = _input_number("K: ")
    col = _input_number("P: ")

    print(f"Row: {' '.join(map(str, mat[row]))}")
    print(f"Column: ", end="")
    _print_mat_col(mat, col)


def task_f3() -> None:
    """ Сформувати матрицю, що складається з нулів и одиниць, причому кількість одиниць строго дорівнює кількості рядків """
    rows = _input_number("Rows: ")
    cols = _input_number("Cols: ")

    total_elements = rows * cols
    elements = [
        *(1 for _ in range(rows)),
        *(0 for _ in range(total_elements - rows)),
    ]
    random.shuffle(elements)

    mat = []
    for row in range(rows):
        mat.append(elements[row * cols:(row + 1) * cols])

    print("Matrix: ")
    _print_mat(mat)


def task_f4() -> None:
    """ У заданій матриці знайти найменший елемент в кожному рядку """
    matrix_size = 5
    mat = _gen_matrix_of_size(matrix_size)

    print("Matrix: ")
    _print_mat(mat)

    for idx, row in enumerate(mat):
        print(f"Minimal element in row {idx}: {min(*row)}")


def task_f5() -> None:
    """ Дана квадратна матриця, що складається з натуральних чисел. Дзеркально відобразити її елементи щодо побічної діагоналі. вивести результат на екран """
    matrix_size = 5
    mat = _gen_matrix_of_size(matrix_size)
    print("Matrix: ")
    _print_mat(mat)

    for i in range(matrix_size):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    print("New matrix: ")
    _print_mat(mat)


def task_g1() -> None:
    """ До вас потрапив зашифрований текст, що означає велику істину для багатьох програмістів. Розшифруйте його, тобто запропонуйте спосіб відновлення початкового тексту і знайдіть цей текст. vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip """
    cipher = "vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf\"uip"
    words = cipher.split(" ")

    a = ord("a")
    A = ord("A")
    z = ord("z")
    Z = ord("Z")
    slash = ord("/")

    az_range = range(a, z + 1)
    AZ_range = range(A, Z + 1)

    key = 3

    # TODO

    for caesar_offset in range(26):
        print(f"Offset: {caesar_offset}, deciphered: ", end="")
        for word in words:
            letters = []
            for idx, letter in enumerate([ord(let) for let in word]):
                if letter in az_range:
                    letter_base = a
                elif letter in AZ_range:
                    letter_base = A
                else:
                    letters.append(letter)
                    continue

                letter_num = letter - letter_base
                letter_num -= caesar_offset
                letter_num %= 26

                letters.append(letter_base + letter_num)

            if not letters:
                continue

            pos = key % len(letters)
            letters = letters[-pos:] + letters[:-pos]

            if slash in letters:
                key += 1

            print("".join(map(chr, letters)), end=" ")

        print()


def _check_all_zeros(mat: list[list[int]], x: int, y: int, w: int, h: int) -> bool:
    if x + w + 1 <= 9:
        w += 1
    if y + h + 1 <= 9:
        h += 1
    if x >= 1:
        x -= 1
    if y >= 1:
        y -= 1

    for i in range(x, x + w + 1):
        for j in range(y, y + h + 1):
            if mat[i][j] != 0:
                return False

    return True


def task_g2() -> None:
    """ Сформувати випадковим чином початкову позицію кораблів для гри "Морський бій" (всього 15 кораблів, один 5-палубний, два 4-палубних, три 3-палубних, чотири 2-палубних, п'ять 1-палубних) на поле 10х10 так, щоб вони не торкалися одне одного """
    mat = [
        [0 for _ in range(10)]
        for _ in range(10)
    ]

    # TODO

    for ship_size in range(5, 0, -1):
        for _ in range(6 - ship_size):
            while True:
                x, y = random.choices(range(10), k=2)
                if random.choice([0, 1]):
                    if y + ship_size >= 10:
                        continue
                    if not _check_all_zeros(mat, x, y, 1, ship_size):
                        continue
                    for i in range(ship_size):
                        mat[x][y + i] = ship_size
                    break
                else:
                    if x + ship_size >= 10:
                        continue
                    if not _check_all_zeros(mat, x, y, ship_size, 1):
                        continue
                    for i in range(ship_size):
                        mat[x + i][y] = ship_size
                    break

            #_print_mat(mat)

    for row in mat:
        for idx, num in enumerate(row):
            if not num:
                row[idx] = "-"

    _print_mat(mat)


def main() -> None:
    task_funcs = (
        #task_a1, task_a2, task_a3,
        #task_b1, task_b2, task_b3,
        #task_c1, task_c2, task_c3, task_c4, task_c5,
        #task_d1, task_d2, task_d3, task_d4, task_d5,
        #task_e1, task_e2, task_e3, task_e4, task_e5,
        #task_f1, task_f2, task_f3, task_f4, task_f5,
        #task_g1, task_g2,

        task_g1,
    )

    for task_func in task_funcs:
        print(f"Task {task_func.__name__.split('_')[1].upper()}")
        task_func()


if __name__ == "__main__":
    main()
