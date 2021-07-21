def solution(arr1, arr2):
    result =[]
    for x,y in zip(arr1, arr2):
        temp = []
        for i in range(0,len(x)):
            temp.append(x[i] + y[i])
        result.append(temp)

    return result


# def sumMatrix(A,B):
#     answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
#     return answer