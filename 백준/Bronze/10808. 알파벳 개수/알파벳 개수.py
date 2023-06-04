import sys

S = [x for x in sys.stdin.readline().strip()]
alphabet = {chr(i): '0' for i in range(ord('a'), ord('z')+1)}
for s in set(S):
    alphabet[s] = str(S.count(s))
print(' '.join(list(alphabet.values())))