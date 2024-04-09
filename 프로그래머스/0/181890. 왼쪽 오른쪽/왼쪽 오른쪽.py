def solution(str_list):
    answer = []
    for i, str in enumerate(str_list):
        if str == "l":
            answer = str_list[:i]
            return answer

        if str == "r":
            answer = str_list[i+1:]
            return answer
    if ["l", "r"] not in str_list:
        return []
    return answer