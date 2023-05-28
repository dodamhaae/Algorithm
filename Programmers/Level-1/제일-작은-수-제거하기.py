def solution(arr):
    arr.remove(min(arr))
    return [-1] if arr==[] else arr