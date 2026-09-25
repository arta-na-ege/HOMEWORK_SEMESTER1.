a = list( map(int, input().split()))
print(*(x for x in a if a.count(x) == 1))