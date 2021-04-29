def num_prime(array):
    number1 = max(array)
    number2 = 2 * number1
    n_list = [0 for _ in range(0, number2 + 1)]
    n_list[0:2] = [1, 1]

    for i in range(2, number2 + 1):
        if n_list[i] == 0:
            j = 2
            while i * j <= number2:
                n_list[i * j] = 1
                j += 1

    for k in array:
        res_list = [i for i, value in enumerate(n_list) if value == 0 and i > k and i <= 2 * k]
        print(len(res_list))

n_list = []
while True:
    n = int(input())
    if n == 0:
        break
    n_list.append(n)

num_prime(n_list)
