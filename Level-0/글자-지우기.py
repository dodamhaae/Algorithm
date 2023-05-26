def solution(my_string, indices):
    return ''.join([s for i,s in enumerate(my_string) if i not in indices])