bword = []
word = input().upper()
aword = list(set(word))
for a in aword:
    bword.append(word.count(a))
if bword.count(max(bword)) > 1:
    print('?')
else:
    index = bword.index(max(bword))
    print(aword[index])