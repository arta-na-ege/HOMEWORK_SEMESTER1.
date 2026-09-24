def calc(n, op):
    res = n[0]
    for x in n[1:]:
        if op == '+':
            res += x
        elif op == '-':
            res -= x
        elif op == '*':
            res *= x
    return res


def to_10(N, old):

    old = int(old)
    decimal = 0
    for ch in str(N):
        decimal = decimal * old + int(ch)
    return decimal

def from_10(decimal, new):
    new = int(new)
    if decimal == 0:
        return '0'

    
    
    digits=[]
    while decimal > 0:
        digits.append(str(decimal % new))
        decimal = decimal // new

    return ''.join(reversed(digits))


with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

nums = lines[0].split()
op = lines[1]
notation = lines[2]

numbers = [to_10(x, notation) for x in nums]
b = calc(numbers,op)
solution = from_10(b, notation)

with open('output.txt', 'w') as f:
    f.write(str(solution))

