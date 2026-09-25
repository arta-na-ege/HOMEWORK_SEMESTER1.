a = list( map(int, input().split()))
max_a  = 0
d = 0
for x in a:
    c = a.count(x)
    if c > max_a:
        max_a = c
        d = x
print(d)