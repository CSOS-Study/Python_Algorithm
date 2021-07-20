result = 0
stack = []


def pick_doll(board, move_num):
    for j in range(0, len(board)):
        if board[j][move_num - 1] != 0:
            temp = board[j][move_num - 1]
            board[j][move_num - 1] = 0
            return temp
    else:
        return False


def put_doll(ret_doll):
    global result
    global stack

    if ret_doll:
        if stack and ret_doll == stack[-1]:
            result += 2
            stack.pop()
        else:
            stack.append(ret_doll)


def solution(board, moves):
    global result

    for i in moves:
        ret_doll = pick_doll(board, i)
        put_doll(ret_doll)

    return result