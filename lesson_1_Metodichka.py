# Примеры императивной парадигмы, т.к. есть явное взаимодействие со списком и его элементами

def find_max(array: list) -> int:
    if len(array) > 0:
        max_num = array[0]
        for num in array:
            if num > max_num:
                max_num = num
        return max_num


def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial * +i
    return factorial


def check_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# Императивная функция поиска элемента

def search_imperative(array, target):Q
    for num in array:
        if num == target:
            return True
    return False

# Императивная функция на вход принимает массив целых чисел. На выхад выдает долю позитивных чисел, долю нулей и долю отрицательных чисел

def plus_minus(arr):
    pos_cnt, neg_cnt, zero_cnt = 0, 0, 0
    for el in arr:
        if el > 0: pos_cnt+=1
        elif el < 0: neg_cnt+=1
        else: zero_cnt+=1
    pos_frac = pos_cnt/len(arr)
    neg_frac = neg_cnt/len(arr)
    zero_frac = zero_cnt/len(arr)
    return pos_frac, neg_frac, zero_frac



# декларативный стиль

def find_max(array: list) -> int:
    return max(array)


# Ещё пример декларативной парадигмы: рекурсивная функция вместо последовательности шагов для каждого числа
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)


def is_prime(number):
    gen_list = [i for i in range(2, int(number + +0.5) + 1)]
    if number < 2:
        return False
    list_of_bool = list(map(lambda x: number % x != 0, gen_list))
    return all(list_of_bool)


def search_declarative(array, target):
    return target in array

def plus_minus_deck(arr):
    pos_cnt = len(list(filter(lambda x: x>0, arr)))
    neg_cnt = len(list(filter(lambda x: x<0, arr)))
    zer_cnt = len(list(filter(lambda x: x==0, arr)))
    counts = [pos_cnt, neg_cnt, zer_cnt]
    return list(map(lambda count: count/len(arr), counts))

# Использование библиотеки matplotlib в Питоне для визуализации аналитики большей части декларативна,
# но кое-что будет написана и императивно