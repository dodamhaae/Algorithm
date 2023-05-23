def solution(strArr):
    for i,n in enumerate(strArr):
        strArr[i]=n.lower() if i%2==0 else n.upper()
    return strArr