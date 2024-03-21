# def solution(arr, queries):
#     answer = []
#     print(arr)
#     arr = arr
#     num_list = []
#     for i in range(len(queries)):
#         for j in range(len(arr)):
#             if queries[i][2] < arr[j]:
#                 num_list.append(arr[j])
#         print(arr.index(min(num_list)))
#         index = arr.index(min(num_list))
#         print(arr)
#         # a = arr.pop(index)
#         # print(a)
#         # a = arr.pop(arr.index(min(num_list)))
#         # print(a)
#         # answer.append(arr.pop(arr.index(min(num_list))))
#         # print(arr.index(min(num_list)))
#         # answer.append(arr.index(min(num_list)))
#     return answer
def solution(arr, queries):
    answer =[]
    for a in queries :
        b = arr[a[0]:a[1]+1]  #쿼리대로 arr에서 리스트를 만듬
        b.sort() #리스트 오름차순 정렬
        for i in b :
            if i> a[2] :
                answer.append(i)
                break
            elif i == b[-1] :
                answer.append(-1)
    return answer