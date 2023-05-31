import sys

M, N = sys.stdin.readline().split()
book = [sys.stdin.readline().strip() for i in range(int(M))]
reverse = {v:i+1 for i,v in enumerate(book)}
for _ in range(int(N)):
    pokemon = sys.stdin.readline().strip()
    print(book[int(pokemon)-1] if pokemon.isdigit() else reverse.get(pokemon))