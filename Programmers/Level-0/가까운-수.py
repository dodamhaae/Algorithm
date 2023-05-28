def solution(array, n):
    array.append(n)
    array.sort()
    i = array.index(n)
    if i==0:
        return array[1]
    elif i==(len(array)-1):
        return array[-2]
    else:
        return array[i-1] if min(array[i]-array[i-1], array[i+1]-array[i])==array[i]-array[i-1] else array[i+1]