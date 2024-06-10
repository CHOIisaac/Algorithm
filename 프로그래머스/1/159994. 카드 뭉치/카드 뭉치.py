def solution(cards1, cards2, goal):
    cards1_i = 0
    cards2_i = 0
    for goal_word in goal:
        if cards1_i < len(cards1) and cards1[cards1_i] == goal_word:
            cards1_i += 1
        elif cards2_i < len(cards2) and cards2[cards2_i] == goal_word:
            cards2_i += 1
        else:
            return "No"
    return "Yes"