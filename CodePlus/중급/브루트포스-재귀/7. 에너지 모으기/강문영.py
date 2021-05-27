n = int(input())
n_list = list(map(int, input().split()))

result_list = []


def extract_energy(marble_list, energy):
    iter_num = len(marble_list)

    if iter_num < 3:
        result_list.append(energy)
        return

    for i in range(1, iter_num - 1):
        temp_energy = energy + marble_list[i - 1] * marble_list[i + 1]
        temp = marble_list.pop(i)
        extract_energy(marble_list, temp_energy)
        marble_list.insert(i, temp)


extract_energy(n_list, 0)
print(max(result_list))