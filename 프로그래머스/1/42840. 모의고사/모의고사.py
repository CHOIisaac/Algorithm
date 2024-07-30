def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    
    for i, a in enumerate(answers):
        if a == one[i % len(one)]:
            count[0] += 1
        if a == two[i % len(two)]:
            count[1] += 1
        if a == three[i % len(three)]:
            count[2] += 1
    
    max_ = max(count)
    max_index = [count.index(max_)+1]
    
    for j, b in enumerate(count):
        if max_ == b:
            answer.append(j+1)
    
    return answer