def solution(rank, attendance):
    answer = 0
    res = []
    num = []
    for i in range(len(rank)):
        if attendance[i]:
            res.append(rank[i])
    for j in sorted(res)[:3]:
        num.append(rank.index(j))
    return 10000 * num[0] + 100 * num[1] + num[2]