def solution(cacheSize, cities):
    cache = []
    result = 0
    if cacheSize == 0:
        return len(cities) * 5

    for cite in cities:
        cite = cite.lower()
        # miss
        if cite not in cache:  # 데이터가 존재하지 않을 경우
            if len(cache) == cacheSize:  # 캐시가 꽉 차있을 경우
                cache.pop(0)
                cache.append(cite)
            else:  # 캐시가 꽉 차 있지 않은 경우
                cache.append(cite)
            result += 5
        # hit
        else:  # 데이터가 존재할 경우
            result += 1
            cache.append(cache.pop(cache.index(cite)))

    return result