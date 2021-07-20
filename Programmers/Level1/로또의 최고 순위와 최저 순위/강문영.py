def solution(lottos, win_nums):
    win_lot_table = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }

    pre_equal_num = [i for i in lottos if i in win_nums]
    potential_num = lottos.count(0)

    worst_grade = win_lot_table[len(pre_equal_num)]
    most_grade = win_lot_table[len(pre_equal_num) + potential_num]

    answer = [most_grade, worst_grade]
    return answer

# set끼리 &연산이 가능하구나..
# def solution(lottos, win_nums):
#     rank = {
#         0: 6,
#         1: 6,
#         2: 5,
#         3: 4,
#         4: 3,
#         5: 2,
#         6: 1
#     }
#     return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]