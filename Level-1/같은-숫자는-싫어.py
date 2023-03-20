def solution(arr):
    answer=[]
    for i in range(1, len(arr)):
        if not arr[i-1] == arr[i]:
            answer.append(arr[i-1])
        if i == len(arr)-1:
            answer.append(arr[i])
    return answer