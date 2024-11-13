import sys

T = int(sys.stdin.readline())
arr = [[0] * 15 for _ in range(15)]

for i in range(15):
    arr[0][i] = i+1

for a in range(1, 15):
    for b in range(15):
        arr[a][b] = arr[a][b-1] + arr[a-1][b]

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(arr[k][n-1])
