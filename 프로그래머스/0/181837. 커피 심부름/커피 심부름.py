def solution(order):
    answer = 0
    for a in order:
        if 'americano' in a or 'anything' in a:
            answer += 4500
        elif 'cafelatte' in a:
            answer += 5000   
    return answer