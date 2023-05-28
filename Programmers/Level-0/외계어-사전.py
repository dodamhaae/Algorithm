def solution(spell, dic):
    spell = list(''.join(sorted(spell)))
    for i in dic:
        if sorted(i) == spell:
            return 1
    return 2