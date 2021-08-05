from itertools import combinations
from collections import defaultdict, Counter


def solution(orders, course):
    result = []
    for i in course:
        menu_dict = defaultdict(int)
        for order in orders:
            for menu in combinations(order, i):
                if len(list(filter(lambda x: x in menu, list(order)))) == len(menu):
                    menu_dict[''.join(sorted(menu))] += 1

        count_menu = Counter(menu_dict).most_common()

        if count_menu:
            max = count_menu[0][1]

            for menu_pick, menu_num in count_menu:
                if menu_num >= 2 and menu_num == max:
                    result.append(''.join(menu_pick))

    return sorted(result)