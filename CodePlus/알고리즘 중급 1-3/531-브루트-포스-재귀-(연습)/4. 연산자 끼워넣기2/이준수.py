import sys
def insert_operator(acc:int, A:list, idx:int, plus:int, minus:int, mul:int, div:int):
    #예외처리 / 답으로써 처리하면 안되는 경우
    if plus < 0 or minus < 0 or mul < 0 or div < 0:
        #최대값과 최소값에 나올수없는 값을 반환한다.
        return (-sys.maxsize, sys.maxsize)

    #남아있는 plus / minus / mul / div 값이 모두 0이상, 더 이상 고를것이 없는 경우 -> 재귀종료
    if N == idx:
        #최대값과 최소값을 정할수없다. 현재값을 최대/최소값으로 반환한다.
        return (acc, acc)

    #더 계산을 해야하는 경우 -> 재귀 진행
    plus_max, plus_min = insert_operator(acc + A[idx], A, idx + 1, plus - 1, minus, mul, div)
    minus_max, minus_min = insert_operator(acc - A[idx], A, idx + 1, plus, minus - 1, mul, div)
    mul_max, mul_min = insert_operator(acc * A[idx], A, idx + 1, plus, minus, mul - 1, div)
    div_max, div_min = insert_operator(int(acc / A[idx]), A, idx + 1, plus, minus, mul, div - 1)
    return (max(plus_max, minus_max, mul_max, div_max),
            min(plus_min, minus_min, mul_min, div_min))


N = int(input())
A = list(map(int,input().split()))
plus, minus, mul, div = map(int,input().split())
mx, mn = insert_operator(A[0], A, 1, plus, minus, mul, div)
print(mx, mn, sep='\n')