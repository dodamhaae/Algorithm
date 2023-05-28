def solution(order):
    return len([0 for x in str(order) if x in '369'])