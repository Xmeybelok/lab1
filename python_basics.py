"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(data):
    text = data.value
    text_lower = text.lower()
    count = 0

    for i in text_lower:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u': count = count + 1
    return count


def has_unique_characters(data):
    text = data.value

    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i] == text[j]: return False
    return True


def count_one_bits(data):
    num = data.value
    count = 0

    while num > 0:
        if num % 2 == 1: count = count + 1
        num = num // 2
    return count


def multiplicative_persistence(data):
    num = data.value
    steps = 0

    while num >= 10:
        prod = 1
        temp = num
        while temp > 0:
            digit = temp % 10
            prod = prod * digit
            temp = temp // 10
        num = prod
        steps = steps + 1
    return steps


def mse(data):
    predicted, expected = data.predicted, data.expected
    n = len(predicted)
    if n == 0: return 0.0
    sum = 0.0
    
    for i in range(n):
        error = predicted[i] - expected[i]
        sum = sum + (error * error)

    return(sum / n)


def prime_factorization(data):
    num = data.value
    result = ""
    d = 2
    
    while d * d <= num:
        if num % d == 0:
            с = 0
            while num % d == 0:
                с = с + 1
                num = num // d
            
            if с == 1:
                result = result + "(" + str(d) + ")"
            else:
                result = result + "(" + str(d) + "**" + str(с) + ")"
        d = d + 1
        
    if num > 1: result = result + "(" + str(num) + ")"
    
    return result


def pyramid(data: PositiveIntegerInput) -> int | str:
    num = data.value
    total = 0
    k = 0

    while total < num:
        k = k + 1
        total = total + (k * k)
    
    if total == num: return k
    else: return "impossible!"

def pyramid(data):
    num = data.value
    total = 0
    k = 0
    while total < num:
        k = k + 1
        total = total + (k * k)
    
    if total == num: return k
    else: return "impossible!"


def is_balanced_num(data):
    num = data.value
    s = str(num)
    left_sum = 0
    right_sum = 0
    k = len(s) // 2
    
    if len(s) % 2 == 1:
        left_part = s[:k]
        right_part = s[k + 1:]
    else:
        left_part = s[:k - 1]
        right_part = s[k + 1:]
    
    for i in left_part: left_sum = left_sum + int(i)

    for i in right_part: right_sum = right_sum + int(i)
    
    return left_sum == right_sum