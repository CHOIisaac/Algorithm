def solution(my_string):
    answer = set()
    result = []
    for a in my_string:
        if a not in answer:
            answer.add(a)
            result.append(a)
            
    return ''.join(result)