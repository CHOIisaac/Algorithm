def solution(arr, query):
    answer = []
    for i ,q in enumerate(query):
        if i % 2 == 0:
            arr = arr[:q+1]
            
        elif i % 2 == 1:
            arr = arr[q:]
    return arr