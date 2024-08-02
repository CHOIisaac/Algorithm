def solution(numbers):
    answer = ''
    nums = list(map(str, numbers))
    nums.sort(key=lambda x: x*10, reverse=True)
    nums_ = ''.join(nums)
    if nums_[0] == '0':
        return '0'
    answer = nums_
    return answer