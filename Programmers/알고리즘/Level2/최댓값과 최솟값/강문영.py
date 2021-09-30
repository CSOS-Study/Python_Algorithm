def solution(s):
    number_list = list(map(int, s.split()))
    max_ = max(number_list)
    min_ = min(number_list)

    return str(min_) + " " + str(max_)