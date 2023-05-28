def solution(rank, attendance):
    arr = sorted([r for i,r in enumerate(rank) if attendance[i]])
    return 10000*rank.index(arr[0]) + 100*rank.index(arr[1]) + rank.index(arr[2])