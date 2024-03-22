def solution(l, r):
    sd = []
    
    for i in range(l,r+1):
        if all(num in ['0','5'] for num in str(i)):
            sd.append(i)
          
    if len(sd) == 0:
        sd.append(-1)  
    return sd   