import sys

list_ = list(map(int, sys.stdin.readline().split()))

while list_ != [1, 2, 3, 4, 5]:
    for i in range(len(list_)-1):
        if list_[i] > list_[i+1]:
            list_[i], list_[i+1] = list_[i+1], list_[i]
            print(' '.join(map(str, list_)))

