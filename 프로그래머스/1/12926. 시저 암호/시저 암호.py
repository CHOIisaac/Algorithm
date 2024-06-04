def solution(s, n):
    answer = ''
    for char in s:
        if char.isalpha():  # 문자가 알파벳인 경우
            # 대문자인 경우
            if char.isupper():
                answer += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            # 소문자인 경우
            else:
                answer += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        else:  # 알파벳이 아닌 경우, 그대로 둠
            answer += char
    return answer