import sys

N = sys.stdin.readline()

one_ = 0
zero_ = 0

if N[0] == '1':
    one_ += 1
elif N[0] == '0':
    zero_ += 1

for i in range(len(N)-1):
    if N[i] != N[i+1]:
        if N[i+1] == '1':
            one_ += 1
        elif N[i+1] == '0':
            zero_ += 1
result = min(one_, zero_)
print(result)