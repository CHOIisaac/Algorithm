from collections import defaultdict

def solution(participant, completion):
    counter = defaultdict(int)
    for comp in completion:
        counter[comp] += 1
    for part in participant:
        if part in counter and counter[part] > 0:
            counter[part] -= 1
        else:
            return part