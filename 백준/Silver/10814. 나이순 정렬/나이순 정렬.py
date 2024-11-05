list_ = []

for i in range(int(input())):
    age, name = input().split()
    age = int(age)
    list_.append((age, name))

# list_.sort(key=lambda x: (x[0], x[2]))
list_.sort(key=lambda x: x[0])

for val in list_:
    print(val[0], val[1])