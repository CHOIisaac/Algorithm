N = int(input())
count = 0
for _ in range(N):
    list_ = []
    for word in input():
        if list_ and list_[-1] == word:
            list_.pop()
        else:
            list_.append(word)
    if not list_:
        count += 1
print(count)