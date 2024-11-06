import sys

list_ = []

for i in range(int(sys.stdin.readline())):
    value = sys.stdin.readline().strip()
    list_.append(value)

list_ = sorted(set(list_), key=lambda x: (len(x), x))

for val in list_:
    print(val)