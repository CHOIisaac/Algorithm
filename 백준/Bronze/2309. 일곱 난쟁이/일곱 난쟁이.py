list_ = []

for _ in range(9):
    value = int(input())
    list_.append(value)

list_.sort()

sum_ = sum(list_)

list1_ = []

found = False

for i in range(9):
    for j in range(i+1, 9):
        if sum_ - (list_[i] + list_[j]) == 100:
            list1_.append(list_[i])
            list1_.append(list_[j])
            found = True
            break
            
    if found:
        break

for val in list_:
    if val in list1_:
        continue
    print(val)