def solution(my_string):
    return [int(x) for x in sorted(my_string) if '0'<=x<='9']