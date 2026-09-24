
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




with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

nums = list(map(int, lines[0].split()))
op = lines[1]

result = calc(nums, op)
with open('output.txt', 'w') as f:
    f.write(str(result))