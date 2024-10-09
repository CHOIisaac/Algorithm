import re

def solution(my_string):
    answer = 0
    numbers = re.findall(r'\d+', my_string)
    answer = sum(map(int, numbers))
    return answer