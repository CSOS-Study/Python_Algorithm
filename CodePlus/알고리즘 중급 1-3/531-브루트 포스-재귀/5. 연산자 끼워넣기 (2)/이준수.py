import sys
def insert_operator(acc:int, A:list, idx:int, plus:int, minus:int, mul:int, div:int):
    if plus < 0 or minus < 0 or mul < 0 or div < 0:
        return

    if N == idx:
        global mx, mn
        mx = max(mx,acc)
        mn = min(mn,acc)
        return

    insert_operator(acc + A[idx], A, idx + 1, plus - 1, minus, mul, div)
    insert_operator(acc - A[idx], A, idx + 1, plus, minus - 1, mul, div)
    insert_operator(acc * A[idx], A, idx + 1, plus, minus, mul - 1, div)
    insert_operator(int(acc / A[idx]), A, idx + 1, plus, minus, mul, div - 1)


N = int(input())
A = list(map(int,input().split()))
plus, minus, mul, div = map(int,input().split())
mx, mn = -sys.maxsize, sys.maxsize
insert_operator(A[0], A, 1, plus, minus, mul, div)
print(mx)
print(mn)