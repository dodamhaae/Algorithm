def solution(numbers):
    for i,n in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine']):
        numbers = numbers.replace(n, str(i))
    return int(numbers)