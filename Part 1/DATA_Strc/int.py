n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    a[i][i] = 0
for r in a:
    print(*r)
