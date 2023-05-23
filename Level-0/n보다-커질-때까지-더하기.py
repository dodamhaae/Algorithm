def solution(numbers, n):
    for i in range(len(numbers)):
        if sum(numbers[:i+1])>n:
            return sum(numbers[:i+1])