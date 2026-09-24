N, b, c = input().split()
b = int(b)
c = int(c)

decimal = 0
for ch in N:
    decimal = decimal * b + int(ch)

if decimal == 0:
    result = 0
else:
    digits=[]
    while decimal > 0:
        digits.append(str(decimal % c))
        decimal = decimal // c
    result = ''.join(reversed(digits))
print(result)
