def solution(myStr):
    answer = []
    for i in ['a', 'b', 'c']:
        myStr = myStr.replace(i, ' ')

    answer = myStr.split()
    if answer == []:
        return ['EMPTY']
    return answer