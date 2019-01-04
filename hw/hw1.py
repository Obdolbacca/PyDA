#  Copyright by Oleg Bobok (c) 2019. For educational purpose

from math import sin, pi
import re
from typing import Tuple


def check_long_is_longer(long_str: str, short_str: str) -> bool:
    return len(long_str) > len(short_str)


def greatest_by_letter_inclusions_count(string: str) -> str:
    string = re.sub(r'[^аи]', '', string)
    ai_len = len(string)
    i_count = len(re.sub(r'[а]', '', string))
    a_count = ai_len - i_count
    return 'а' if a_count > i_count else 'и'


def bytes_to_megabytes(volume: int) -> float:
    megabytes: float = float(volume) / (1024*1024)
    return round(megabytes, 2)


def swap(param_a: int, param_b: int) -> Tuple[int, int]:
    return param_b, param_a


def bin_to_dec(value: int) -> int:
    result_value: int = 0
    string_to_parse: str = ''.join(reversed(str(value)))
    for i in range(len(string_to_parse)):
        if string_to_parse[i] == '1':
            result_value += pow(2, i)
    return result_value


if __name__ == '__main__':
    long_phrase: str = 'Насколько проще было бы писать программы, если бы не заказчики'
    short_phrase: str = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
    result: bool = check_long_is_longer(short_str=short_phrase, long_str=long_phrase)
    print('{0}'.format(result))

    text: str = 'Если программист в 9-00 утра на работе, значит, он там и ночевал'
    print('{0}'.format(greatest_by_letter_inclusions_count(text)))

    print('Объем файла равен {0}Mb'.format(bytes_to_megabytes(217000000)))

    print('{0}'.format(sin(pi/6)))

    print('{0}'.format(0.1 + 0.2))

    a: int = 1
    b: int = 3
    print('{0} -> {1}'.format(a, b))
    a, b = swap(a, b)
    print('{0} -> {1}'.format(a, b))

    print('{0}'.format(bin_to_dec(110111)))
    print('done')
