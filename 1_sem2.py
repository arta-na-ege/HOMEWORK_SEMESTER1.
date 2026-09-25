
d = list(map(int, input().split()))
print(d[0] * (d[0] + 1) // 2 - sum(d) + d[0])

