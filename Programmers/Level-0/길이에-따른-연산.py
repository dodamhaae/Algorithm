from math import prod
def solution(num_list):
    return prod(num_list) if len(num_list)<11 else sum(num_list)