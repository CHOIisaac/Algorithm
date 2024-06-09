def solution(name, yearning, photo):
    answer = []
    for persons in photo:
        score = 0
        for person in persons:
            if person in name:
                index = name.index(person)
                score += yearning[index]
        answer.append(score)
    return answer