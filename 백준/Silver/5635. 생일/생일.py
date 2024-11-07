import sys

list_ = []

for i in range(int(sys.stdin.readline())):
    name, day, month, year = sys.stdin.readline().split()
    list_.append([name, int(day), int(month), int(year)])

list_ = sorted(list_, key=lambda x: (x[3], x[2], x[1]))

print(list_[-1][0])
print(list_[0][0])