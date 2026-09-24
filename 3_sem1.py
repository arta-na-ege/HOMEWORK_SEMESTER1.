#считаю, что все операции над натуральными числами, если это не так, то вместо int в 3 строке надо вписать float

a = list(map(int, input().split()))


pr = 1
n = len(a)


for x in a:
    pr *= x
print(pr**(1 / n))
