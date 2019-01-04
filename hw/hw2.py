#  Copyright by Oleg Bobok (c) 2019. For educational purpose

"""
Module with second homework
"""

from typing import List, Dict, Union


def sort_visits_dict_by_country(visits):
    """
    Get visits from Russia
    :type visits: Dict[str, List[str, str]]
    :param visits: Dict with all visits
    :rtype: Dict[str, List[str, str]]
    :return: Visits from Russia
    """
    result = {}
    for key, value in visits.items():
        if value[1] == 'Россия':
            result.update({key: value})

    return result


def get_unique_ids(ids: Dict[str, List[int]]) -> List[int]:
    """
    Get unique IDs
    :param ids: Dict with IDs per user
    :return: List of unique IDs
    """
    l: list = ids.values()
    ret_l = [item for sublist in l for item in sublist]
    return list(set(ret_l))


def get_query_distribution(queries_param: List[str]) -> Dict[str, str]:
    """
    Get query distribution
    :param queries_param: List of queries
    :return: Dict with percentage of queries per length in words
    """
    words: List[List[str]] = []
    for query in queries_param:
        words.append(query.split(' '))

    ret_d: dict = {}
    for ar in words:
        ret_d.update({str(len(ar)): (ret_d.get(str(len(ar)), None) or 0) + 1})

    all_occurrences = sum(ret_d.values())

    final: dict = {}
    for k, v in ret_d.items():
        final[k] = str(round(v * 100 / all_occurrences)) + '%'

    return final


def get_channel_with_max_volume(stats: Dict[str, int]) -> str:
    """
    Get channel with maximal volume
    :param stats: Dict with stats
    :return: Name of channel
    """
    max_volume_channel = ['', 0]
    for k, v in stats.items():
        if int(v) > max_volume_channel[1]:
            max_volume_channel = [k, v]
    return max_volume_channel[0]


def avg_views_per_user(stream: List[str]) -> float:
    """
    Count average amount of views per user
    :param stream: Stream of user views
    :return: Average amount of views per user
    """
    unique_users = set()
    counter = 0
    for visit in stream:
        visit_parsed = visit.split(',')
        unique_users.add(visit_parsed[1])
        counter += int(visit_parsed[2])

    return counter / len(unique_users)


def search_by_date_and_company(stats: List[Union[int, str]], date_param: str, company_param: str):
    """
    Search stats for given company and date
    :param stats: Stats list
    :param date_param: Date to search
    :param company_param: Company name
    :rtype: int
    :return: Amount from stats for given company and date
    """
    date_company = {stat[0] + '_' + stat[1]: stat[2] for stat in stats}
    return date_company[date_param + '_' + company_param]


if __name__ == '__main__':
    geo_logs = {
        'visit1': ['Москва', 'Россия'],
        'visit2': ['Дели', 'Индия'],
        'visit3': ['Владимир', 'Россия'],
        'visit4': ['Лиссабон', 'Португалия'],
        'visit5': ['Париж', 'Франция'],
        'visit6': ['Лиссабон', 'Португалия'],
        'visit7': ['Тула', 'Россия'],
        'visit8': ['Тула', 'Россия'],
        'visit9': ['Курск', 'Россия'],
        'visit10': ['Архангельск', 'Россия'],
    }

    print(sort_visits_dict_by_country(geo_logs))

    ids = {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]}

    print('{0}'.format(get_unique_ids(ids)))

    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт',
        'хрень'
    ]

    print('{0}'.format(get_query_distribution(queries)))

    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

    print('{0}'.format(get_channel_with_max_volume(stats)))

    stream = [
        '2018-01-01,user1,3',
        '2018-01-07,user1,4',
        '2018-03-29,user1,1',
        '2018-04-04,user1,13',
        '2018-01-05,user2,7',
        '2018-06-14,user3,4',
        '2018-07-02,user3,10',
        '2018-03-21,user4,19',
        '2018-03-22,user4,4',
        '2018-04-22,user4,8',
        '2018-05-03,user4,9',
        '2018-05-11,user4,11',
    ]

    print(avg_views_per_user(stream))

stats = [
    ['2018-01-01', 'google', 25],
    ['2018-01-01', 'yandex', 65],
    ['2018-01-01', 'market', 89],
    ['2018-01-02', 'google', 574],
    ['2018-01-02', 'yandex', 249],
    ['2018-01-02', 'market', 994],
    ['2018-01-03', 'google', 1843],
    ['2018-01-03', 'yandex', 1327],
    ['2018-01-03', 'market', 1764],
]

print(search_by_date_and_company(stats, '2018-01-02', 'google'))

