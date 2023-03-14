def solution(arr, divisor):
    return [i for i in sorted(arr) if i%divisor==0] or [-1]