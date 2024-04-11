def solution(todo_list, finished):
    answer = []
    # answer = answer.append(todo_list[i]) if finished[i] == false for i in range(len(todo_list))
    for i in range(len(todo_list)):
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer