import sys

bingo_list = []
call_list = []
for i in range(10):
    num = list(map(int, sys.stdin.readline().split()))
    if i < 5:
        bingo_list.append(num)
    else:
        call_list.extend(num)

def check_bingo(bingo_list):
    count = 0
    for k in range(5):
        if all(bingo_list[k][h] == 0 for h in range(5)):
            count += 1

    for h in range(5):
        if all(bingo_list[k][h] == 0 for k in range(5)):
            count += 1

    if all(bingo_list[k][k] == 0 for k in range(5)):
        count += 1
    if all(bingo_list[k][4 - k] == 0 for k in range(5)):
        count += 1
    return count


for i in range(len(call_list)):
    for j in range(len(bingo_list)):
        for k in range(len(bingo_list)):
            if call_list[i] == bingo_list[j][k]:
                bingo_list[j][k] = 0

    if check_bingo(bingo_list) >= 3:
        print(i+1)
        break