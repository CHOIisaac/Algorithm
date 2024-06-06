def solution(n, arr1, arr2):
    answer = []
    res = ''
    for i in range(n):
        res = ''
        a = bin(arr1[i])[2:].zfill(n)
        b = bin(arr2[i])[2:].zfill(n)
        
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                res += '#'
            else:
                res += ' '
        answer.append(res)
    return answer