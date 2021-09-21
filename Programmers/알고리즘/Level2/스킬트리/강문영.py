def solution(skill, skill_trees):
    result = 0

    for user_skill in skill_trees:
        stack = []
        is_okay = True

        for each_skill in user_skill:
            if each_skill in list(skill):  # 새로 배우려는 스킬이 선행스킬에 있다.
                if set(list(skill[:skill.index(each_skill)])) - set(stack):
                    is_okay = False
                    break
                for already_skill in stack:  # 이미 스택에 들어간 스킬들 중에 순서가 더 느린게 있다면?
                    if already_skill in skill and skill.index(each_skill) < skill.index(already_skill):
                        is_okay = False
                        break
                else:
                    stack.append(each_skill)

            if not is_okay:
                break
        else:
            print(user_skill)
            result += 1

    return result