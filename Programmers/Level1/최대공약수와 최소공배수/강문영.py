def extract_max(x, y):
    while y > 0:
        x, y = y, x % y
    return x
## 최대 공약수 공식 외우자 

def solution(n, m):
    max_num = extract_max(n, m)
    min_num = n * m // max_num
    return [max_num, min_num]