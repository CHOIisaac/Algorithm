hour, minute = map(int, input().split())

minute -= 45

if minute < 0:
    minute += 60  # 60분을 더해서 양수로 만들기
    hour -= 1     # 시간을 1 감소

    if hour < 0:
        hour = 23

print(hour, minute)