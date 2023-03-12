def solution(my_string):
    return sum([int(x) for x in my_string if '0'<=x<='9'])