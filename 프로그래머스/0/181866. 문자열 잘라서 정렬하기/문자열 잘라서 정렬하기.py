def solution(myString):
    answer = myString.split('x')
    aaa = []
    for a in answer:
        if a == '':
            continue
        else:
            aaa.append(a)
    return sorted(aaa)