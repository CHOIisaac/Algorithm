import sys


N = int(sys.stdin.readline())

list_ = []

for _ in range(N):
    count = 0
    card_list = list(map(int, sys.stdin.readline().split()))

    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                num = (card_list[i] + card_list[j] + card_list[k]) % 10
                if num >= count:
                    count = num
    list_.append(count)

for i in range(len(list_)-1, -1, -1):
    if list_[i] == max(list_):
        print(i + 1)
        break