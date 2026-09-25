G, a = input().split()
G = int(G)
b = len(a)//G
out = ''
for i in range(0,len(a), b):
    out += a[i:i+b][::-1]
print(out)
