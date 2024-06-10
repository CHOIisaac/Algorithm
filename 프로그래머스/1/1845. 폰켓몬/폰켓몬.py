def solution(nums):
    count = 0
    size_count = {}
    for size in nums:
        if size in size_count:
            size_count[size] += 1
        else:
            size_count[size] = 1
    print(size_count)
    sorted_counts = sorted(size_count.values(), reverse=True)
    print(sorted_counts)
    you_take = int(sum(sorted_counts)/2)
    print(you_take)
    answer = min(you_take,len(sorted_counts))
    print(answer)
    return answer