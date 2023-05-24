def solution(arr, query):
    for i in range(len(query)):
        arr = arr[:query[i]+1] if i%2==0 else arr[query[i]:]
    return arr