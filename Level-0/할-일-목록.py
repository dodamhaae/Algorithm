def solution(todo_list, finished):
    return [t for i,t in enumerate(todo_list) if not finished[i]]