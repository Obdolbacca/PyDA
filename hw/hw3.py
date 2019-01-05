#  Copyright by Oleg Bobok (c) 2019. For educational purpose

"""
Module for third homework
"""

from typing import List, Union

import requests
import json
from hw import HttpException


def diag_sum(data_param: List[List[int]]) -> int:
    """
    Diagonal sum
    :param data_param: NxN array of integers
    :return: Sum of diagonal elements
    """
    return sum([data_param[i][i] for i in range(len(data_param))])


def square_list(data_param: List[Union[int, str]]) -> int:
    """
    Sum of squares
    :param data_param: list of integers and strings
    :return: sum of squares of all elements possible
    """
    numbers: List[int] = []
    for elem in data_param:
        try:
            numbers.append(int(elem) ** 2)
        except ValueError:
            pass

    return sum(numbers)


'''
Хотел поиграть с генераторами
'''


class Fibonacci:
    """
    Class for calculation of N first fibonacci numbers and its' sum
    """
    def __init__(self, num_iterations: int):
        self._num_iterations = num_iterations

    def _gen_fib(self) -> List[int]:
        a, b = 0, 1
        for _ in range(1, self._num_iterations + 1):
            a, b = b, a + b
            yield a

    def fib(self):
        """
        List of first fibonacci numbers
        :rtype: List[int]
        :return: list with n fibonacci numbers
        """
        return list(self._gen_fib())

    def sum_fib(self):
        """
        Sum of first fibonacci numbers
        :rtype: int
        :return: sum of first N fibonacci numbers
        """
        return sum(self.fib())


class CurrencyProcessor:
    """
    Class for processing https://www.cbr-xml-daily.ru/daily_json.js
    """
    def __init__(self):
        """
        :rtype: None
        :exception HttpException
        """
        self._response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        if self._response.status_code != 200:
            raise HttpException(1)

    def get_currency_name(self) -> str:
        """
        Currency name with greatest rate
        :return: Name of currency with highest rate
        """
        ret = json.loads(self._response.text)
        rate: List[str, float] = ['', 0.0]
        for currency_name, currency in dict(ret['Valute']).items():
            if currency['Value'] > rate[1]:
                rate = [currency_name, currency['Value']]

        return ret['Valute'][rate[0]]['Name']


if __name__ == '__main__':
    data = [
        [13, 25, 23, 34],
        [45, 32, 44, 47],
        [12, 33, 23, 95],
        [13, 53, 34, 35],
    ]

    print(diag_sum(data))

    data = [1, '5', 'abc', 20, '2']

    print(square_list(data))

    print(CurrencyProcessor().get_currency_name())

    print(Fibonacci(8).sum_fib())
