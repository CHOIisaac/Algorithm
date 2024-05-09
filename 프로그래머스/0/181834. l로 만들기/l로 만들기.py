def solution(myString):
    answer = ''
    for i in range(len(myString)):

        if myString[i] < 'l':
            myString = myString.replace(myString[i], 'l')
    return myString