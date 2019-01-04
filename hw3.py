from typing import List, Union


def diag_sum(data: List[List[int]]) -> int:
    return sum([data[i][i] for i in range(len(data))])


def square_list(data: List[Union[int, str]]) -> int:
    numbers: List[int] = []
    for elem in data:
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
        for i in range(1, self._num_iterations + 1):
            yield a
            a, b = b, a + b

    def fib(self):
        return list(self.gen_fib())


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

    print(Fibonacci(8).fib())
