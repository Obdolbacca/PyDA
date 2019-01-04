#  Copyright by Oleg Bobok (c) 2019. For educational purpose

from typing import List, Union

import requests
import json


def diag_sum(data_param: List[List[int]]) -> int:
    return sum([data_param[i][i] for i in range(len(data))])


def square_list(data_param: List[Union[int, str]]) -> int:
    numbers: List[int] = []
    for elem in data_param:
        try:
            numbers.append(int(elem))
        except ValueError:
            pass

    return sum(numbers)


'''
Хотел поиграть с генераторами
'''


class Fibonacci:
    def __init__(self, num_iterations: int):
        self._num_iterations = num_iterations

    def gen_fib(self) -> List[int]:
        a, b = 0, 1
        for _ in range(1, self._num_iterations + 1):
            a, b = b, a + b
            yield a

    def fib(self):
        return sum(list(self.gen_fib()))


def get_currency_name() -> str:
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    ret = json.loads(response.text)
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

    print(get_currency_name())

    print(Fibonacci(8).fib())
