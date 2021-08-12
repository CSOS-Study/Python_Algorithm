def solution(bridge_length, weight, truck_weights):
    truck_go_len = [weight / i for i in truck_weights]
    time = 0
    for i in truck_go_len:
        time += 1
        if i < bridge_length:
            time += 1

    print(time)
    return time


solution(2, 10, [7, 4, 5, 6])
