from typing import Callable
from functools import reduce
import re


def generator_numbers(text: str): # returns generator
    # Using lazy re.finditer() and map() to yield numbers one by one
    matches = re.finditer(r"\s*[-+]?\d*.\d+\s*", text)

    for match in matches:
        yield float(match.group().strip())


def numbers(text: str): # returns lazy iterator and behaves similarly to a generator
    # Using lazy re.finditer() and map() to yield numbers one by one
    matches = re.finditer(r"\s*[-+]?\d*.\d+\s*", text)
    numbers = map(lambda match: float(match.group().strip()), matches)

    return numbers


def sum_profit(text: str, func: Callable):
    incomes = func(text)
    total = reduce(lambda prev, curr: prev + curr, incomes)

    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
