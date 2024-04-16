def solution(babbling):
    answer = 0
    a = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for j in a:
            babbling[i] = babbling[i].replace(j, ' ')
        babbling[i] = babbling[i].replace(' ', '')

    return babbling.count('')