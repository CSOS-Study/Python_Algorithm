from collections import deque


def solution(cacheSize, cities):
    cache_hit = 1
    cache_miss = 5
    time = 0

    cache = []

    if cacheSize == 0:
        return cache_miss * len(cities)
    for city in cities:
        if city.lower() not in cache:  # 데이터가 없을 경우
            if len(cache) == cacheSize:  # 꽉 차있는 경우
                cache.pop(0)
                cache.append(city.lower())
                time += cache_miss
            else:  # 꽉 안차있는 겨우
                cache.append(city.lower())
                time += cache_miss
        else:  # 데이터가 있는 경우
            cache.append(cache.pop(cache.index(city.lower())))
            time += 1

    return time

# 스택의 개념을 잊지말자