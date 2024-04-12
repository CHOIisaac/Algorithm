def solution(arr):
    idx = 0  # x의 값을 저장할 변수
    prev = arr  # 현재 배열을 저장할 변수
    
    while True:
        change = []  # 작업을 통해 변경된 배열을 저장할 리스트
        for i in prev:
            if i >= 50 and i % 2 == 0: 
                change.append(int(i / 2))  # 값이 50보다 크고 짝수인 경우 2로 나눈다
                
            elif i < 50 and i % 2 == 1: 
                change.append(i * 2 + 1)  # 값이 50보다 작고 홀수인 경우 2를 곱하고 1을 더한다
                
            else: 
                change.append(i)  # 나머지 경우에는 그대로 유지
        
        same = all(a == b for a, b in zip(prev, change))  # 현재 배열과 변경된 배열이 동일한지 확인
        
        if same:
            break  # 현재 배열과 변경된 배열이 동일하다면 반복을 종료하고 x 반환
        idx += 1  # x 값을 증가
        prev = change  # 변경된 배열을 현재 배열로 업데이트
        
    return idx