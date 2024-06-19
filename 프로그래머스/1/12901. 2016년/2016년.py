from datetime import datetime

def solution(a, b):
    days_of_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    input_date = datetime(2016, a, b)
    day_of_week = days_of_week[input_date.weekday()]
    return day_of_week