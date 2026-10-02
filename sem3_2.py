n = int(input())

def simple(N):
    d = 2

    a = []
    while d <= N**0.5:
        if N % d == 0: 
            a.append(d)
            N = N // d
        else: d += 1
    a.append(N)
    return a
print(simple(n))