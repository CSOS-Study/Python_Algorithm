def dfs(num):

    if num >=5:
        print("리턴")
        print(num)
        return
    print("+1 호출하기 전")
    print(num)
    dfs(num+1)
    print("+1 리턴 후, -1 호출")
    print(num)
    dfs(num+2)

dfs(1)