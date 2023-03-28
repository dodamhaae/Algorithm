def solution(price, money, count):
    answer=0
    for i in range(count):
        answer+=price*(i+1)
    return 0 if answer<=money else answer-money